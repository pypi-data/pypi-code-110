from typing import List, NamedTuple, Optional, Union

import htmlgenerator as hg
from django.db import models
from htmlgenerator import Lazy

from .urls import model_urlname
from .urls import reverse as urlreverse


class LazyHref(hg.Lazy):
    """An element which will resolve lazy. The ``args`` and ``kwargs`` arguments will
    be passed to ``bread.utils.urls.reverse``. Every (lazy) item in ``args`` will be
    resolved and every value in ``kwargs`` will be resolved.

    Example usage:

        assert "/settings" == LazyHref(hg.F(lambda c: "settings"))

    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def resolve(self, context: dict):
        kwargs = {k: hg.resolve_lazy(v, context) for k, v in self.kwargs.items()}
        # the django reverse function requires url-keyword arguments to be pass
        # in a parameter named "kwarg". This is a bit confusing since kwargs
        # normally referse to the python keyword arguments and not to URL
        # keyword arguments. However, we also want to support lazy URL
        # keywords, so we do the resolving of the actualy URL-kwargs as well
        if "kwargs" in kwargs:
            kwargs["kwargs"] = {
                k: hg.resolve_lazy(v, context) for k, v in kwargs["kwargs"].items()
            }
        if "query" in kwargs:
            kwargs["query"] = {
                k: hg.resolve_lazy(v, context) for k, v in kwargs["query"].items()
            }
        if "args" in kwargs:
            kwargs["args"] = [hg.resolve_lazy(arg, context) for arg in kwargs["args"]]
        return urlreverse(*[hg.resolve_lazy(a, context) for a in self.args], **kwargs)


class ModelHref(LazyHref):
    """
    Works similar to LazyHref but takes a model and a model action
    like "edit", "read", "browse" and generates the URL automatically
    (according to bread conventions).
    This is usefull as a replacment of wrapping ``bread.utils.urls.reverse_model``
    inside a hg.F element for lazy evalutation of the pk value.

    Example usage:

        assert "/person/browse" == ModelHref(models.Person, "browse").resolve(context)
        assert "/person/edit/1" == ModelHref(
            models.Person, "edit", kwargs={"pk": hg.C("object.pk")}
        ).resolve(context)

    """

    def __init__(self, model, name, *args, **kwargs):
        # if this is an instance of a model, we can extract the pk URL argument directly
        # TODO: instance-specific routes which don't use the pk argument will fail
        if isinstance(model, models.Model) and "pk" not in kwargs.get("kwargs", {}):
            if "kwargs" not in kwargs:
                kwargs["kwargs"] = {}
            kwargs["kwargs"]["pk"] = model.pk

        if isinstance(model, hg.Lazy):
            url = hg.F(lambda c: model_urlname(hg.resolve_lazy(model, c), name))
        else:
            url = model_urlname(model, name)

        super().__init__(url, *args, **kwargs)


def try_call(var, *args, **kwargs):
    return var(*args, **kwargs) if callable(var) else var


class Link(NamedTuple):
    href: Union[str, Lazy]
    label: str
    iconname: Optional[str] = "fade"
    permissions: List[str] = []
    attributes: dict = {}

    def has_permission(self, request, obj=None):
        return all(
            [
                request.user.has_perm(perm, obj) or request.user.has_perm(perm)
                for perm in self.permissions
            ]
        )
