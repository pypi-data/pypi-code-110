import json
from asyncio import Queue
from inspect import isfunction
from typing import Dict
from threedi_api_client.openapi.api.v3_api import V3Api
from threedi_api_client.openapi.models import Schematisation, Simulation
from pathlib import Path
import requests
from rich.live import Live

from threedi_cmd.console import console
from threedi_cmd.models.errors import ApiModelError
from threedi_cmd.logger import get_logger

logger = get_logger("INFO")


def evaluate_lazy(value):
    if isfunction(value):
        return value()
    return value


def class_repr(data, model):
    params = ", ".join(
        [
            f"{key}={json.dumps(str(evaluate_lazy(value)))}"
            for key, value in data.items()
        ]
    )
    return f"{model.__name__}({params})"


class BaseWrapper:
    def __init__(
        self,
        data: Dict,
        api_client: V3Api,
        base_path: Path = None,
        refs: Dict = None,
    ):
        self._api_client = api_client
        self._data = data
        self._base_path = base_path
        self._refs = refs

    async def execute(self, queue: Queue):
        pass

    @property
    def extra_steps(self):
        return []


BLACKLIST = {
    "waitfor_timeout",
}


class ModelWrapper(BaseWrapper):
    api_path: str = None
    instance: object = None
    _internal_state = None
    model: object = None
    scenario_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize_instance(self._data)
        self.api: V3Api = self._api_client  # noqa

        # Add self to refs
        if "_ref" in self._data:
            self._refs[self._data["_ref"]] = self.instance

    def resolve_func_name(self, suffix: str):
        func = getattr(self._api_client, f"{self.api_path}{suffix}")
        return func

    def initialize_instance(self, data: Dict):
        """raises ApiModelError if initializing the instance fails"""
        new_data = {
            key: value
            for key, value in data.items()
            if not key.startswith("_") and key not in BLACKLIST
        }
        try:
            self.instance = self.model(**new_data)
        except ValueError as err:
            msg = f"Initializing {self.model.__name__} failed: {err}"
            raise ApiModelError(msg)

    async def execute(self, queue):
        # By default save()
        self.save()
        for step in self.extra_steps:
            await step.execute(queue)

    def create(self):
        with Live(console=console) as live:
            live.update(f"Creating {self.model.__name__}...")
            func = self.resolve_func_name("_create")
            res = func(self.instance)
            live.update(
                f":heavy_check_mark: [bold spring_green4] Created {self.model.__name__}"
            )
        console.print(self._data)
        return res

    def patch(self, data):
        with Live(console=console) as live:
            live.update(f"Patching {self.model.__name__}...")
            func = self.resolve_func_name("_partial_update")
            res = func(self.instance.id, data)
            live.update(
                f":heavy_check_mark: [bold spring_green4] Patched {self.model.__name__}"
            )
        console.print(self._data)
        return res

    def delete(self):
        with Live(console=console) as live:
            live.update(f"Deleting {self.model.__name__}...")
            func = self.resolve_func_name("_delete")
            res = func(self.instance.id)
            live.update(
                f":heavy_check_mark: [bold spring_green4] Deleted {self.model.__name__}"
            )
        return res

    def save(self):
        res = None
        id = getattr(self.instance, "id", None)

        if id is None:
            # Create
            res = self.create()
        else:
            # Update (use patch by default)
            old_set = set(self._internal_state.to_dict().items())
            new_set = set(self.instance.to_dict().items())

            diff = new_set - old_set

            if diff != set():
                # There is something we can try to update
                res = self.patch(dict(diff))

        if res is not None:
            # Update values of self to match what has been returned
            for key, value in res.to_dict().items():
                if hasattr(self.instance, key) and value is not None:
                    setattr(self.instance, key, value)

            self._internal_state = res

    def __repr__(self):
        return class_repr(self._data, self.model)


class SimulationWrapper(ModelWrapper):
    model = Simulation
    api_path = "simulations"


class SchematisationWrapper(ModelWrapper):
    model = Schematisation
    api_path = "schematisations"


class SimulationChildWrapper(ModelWrapper):
    simulation = None
    base_path = "simulations_"

    def __init__(self, *args, **kwargs):
        self.simulation = kwargs.pop("simulation", None)
        super().__init__(*args, **kwargs)

    @property
    def instance_name(self):
        return self.scenario_name

    def resolve_func_name(self, suffix: str):
        func = getattr(self._api_client, f"{self.base_path}{self.api_path}{suffix}")
        return func

    def create(self, *args, **kwargs):
        with Live(console=console) as live:
            live.update(f"Creating {self.model.__name__}...")
            func = self.resolve_func_name("_create")
            res = func(self.simulation.id, self.instance, *args, **kwargs)
            live.update(
                f":heavy_check_mark: [bold spring_green4] Created {self.model.__name__}"
            )
        console.print(self._data)
        return res

    def patch(self, data):
        with Live(console=console) as live:
            live.update(f"Patching {self.model}...")
            func = self.resolve_func_name("_partial_update")
            res = func(self.instance.id, self.simulation.id, data)
            live.update(f":heavy_check_mark: [bold spring_green4] Patched {self.model}")
        return res

    def delete(self):
        func = self.resolve_func_name("_delete")
        res = func(self.instance.id, self.simulation.id)
        logger.debug("Deleted %s with id: %s", self.instance_name, self.instance.id)
        return res


class SchematisationChildWrapper(ModelWrapper):
    schematisation = None
    base_path = "schematisations_"

    def __init__(self, *args, **kwargs):
        self.schematisation = kwargs.pop("schematisation", None)
        super().__init__(*args, **kwargs)

    def resolve_func_name(self, suffix: str):
        func = getattr(self._api_client, f"{self.base_path}{self.api_path}{suffix}")
        return func

    @property
    def instance_name(self):
        return self.scenario_name

    def create(self, *args, **kwargs):
        with Live(console=console) as live:
            live.update(f"Creating {self.model.__name__}...")
            func = self.resolve_func_name("_create")
            res = func(self.schematisation.id, self.instance, *args, **kwargs)
            live.update(
                f":heavy_check_mark: [bold spring_green4] Created {self.model.__name__}"
            )
        console.print(self._data)
        return res

    def patch(self, data):
        with Live(console=console) as live:
            live.update(f"Patching {self.model}...")
            func = self.resolve_func_name("_partial_update")
            res = func(self.instance.id, self.schematisation.id, data)
            live.update(f":heavy_check_mark: [bold spring_green4] Patched {self.model}")
        return res

    def delete(self):
        func = self.resolve_func_name("_delete")
        res = func(self.instance.id, self.schematisation.id)
        logger.debug("Deleted %s with id: %s", self.instance_name, self.instance.id)
        return res


class RevisionChildWrapper(SchematisationChildWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resolve_func_name(self, suffix: str):
        func = getattr(self._api_client, f"{self.base_path}{self.api_path}{suffix}")
        return func

    @property
    def revision(self):
        """
        Try to resolve revision based
        on _revision reference
        """
        revision_ref = self._data["_revision"]
        return self._refs[revision_ref]

    @property
    def instance_name(self):
        return self.scenario_name

    def create(self, *args, **kwargs):
        with Live(console=console) as live:
            live.update(f"Creating {self.model.__name__}...")
            func = self.resolve_func_name("_create")
            res = func(
                self.revision.id, self.schematisation.id, self.instance, *args, **kwargs
            )
            live.update(
                f":heavy_check_mark: [bold spring_green4] Created {self.model.__name__}"
            )
        console.print(self._data)
        return res

    def patch(self, data):
        with Live(console=console) as live:
            live.update(f"Patching {self.model}...")
            func = self.resolve_func_name("_partial_update")
            res = func(self.instance.id, self.schematisation.id, data)
            live.update(f":heavy_check_mark: [bold spring_green4] Patched {self.model}")
        return res

    def delete(self):
        func = self.resolve_func_name("_delete")
        res = func(self.instance.id, self.schematisation.id)
        logger.debug("Deleted %s with id: %s", self.instance_name, self.instance.id)
        return res

    def _upload_file(self, put_url=None):
        if not hasattr(self, "filepath") or not self.filepath:
            return
        if put_url is None:
            put_url = self.instance.put_url

        filepath = Path(self.filepath)
        if self._base_path:
            filepath = self._base_path / filepath
        fp = (filepath).resolve()
        # Upload file
        with fp.open("rb") as f:
            res = requests.put(put_url, data=f)
            assert res.status_code == 200

    def save(self, upload_file=True):
        super().save()

        if upload_file:
            self._upload_file()


class EventWrapper(SimulationChildWrapper):
    base_path = "simulations_events_"

    def save(self):
        super().save()

        if not hasattr(self, "filepath") or not self.filepath:
            return
        filepath = Path(self.filepath)
        if self._base_path:
            filepath = self._base_path / filepath
        fp = (filepath).resolve()

        # Upload file
        with fp.open("rb") as f:
            res = requests.put(self.instance.put_url, data=f)
            assert res.status_code == 200


class SettingsWrapper(SimulationChildWrapper):
    base_path = "simulations_settings_"


class InitialWrapper(SimulationChildWrapper):
    base_path = "simulations_initial_"
