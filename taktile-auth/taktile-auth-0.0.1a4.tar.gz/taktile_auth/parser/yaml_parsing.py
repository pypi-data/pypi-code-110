import pathlib
import typing as t

import yaml

from taktile_auth.entities import (
    PermissionDefinition,
    ResourceDefinition,
    RoleDefinition,
)
from taktile_auth.parser.utils import parse_body


def parse_role(
    role_name: str,
    role_yaml: t.Dict[str, t.Any],
    resources: t.Dict[str, ResourceDefinition],
) -> "RoleDefinition":
    perm_definitions = []
    sub_role_definitions = []
    role_args = role_yaml[role_name]["role_args"]
    role_body = role_yaml[role_name]["role_body"]
    clauses = parse_body(role_body)
    for clause in clauses:
        if clause["type"] == "permission":
            perm_definitions.append(
                PermissionDefinition(
                    actions=set(clause["actions"]),
                    resource_definition=resources[clause["resource_name"]],
                )
            )
        else:
            sub_role_definitions.append(
                parse_role(clause["sub_role_name"], role_yaml, resources)
            )
    return RoleDefinition(
        name=role_name,
        permission_definitions=perm_definitions,
        args=role_args,
        sub_role_definitions=sub_role_definitions,
    )


def parse_resource_yaml(path: pathlib.Path) -> t.Dict[str, ResourceDefinition]:
    with open(path, "rb") as f:
        resources_yaml = yaml.safe_load(f)
    resources: t.Dict[str, ResourceDefinition] = {}
    for resource_name, args in resources_yaml.items():
        resources[resource_name] = ResourceDefinition(
            resource_name=resource_name, args=args
        )
    return resources


def parse_role_yaml(
    role_path: pathlib.Path, resource_path: pathlib.Path
) -> t.Dict[str, RoleDefinition]:
    roles: t.Dict[str, RoleDefinition] = {}
    role_yaml = {}
    resources = parse_resource_yaml(resource_path)
    with open(role_path, "rb") as f:
        roles = yaml.safe_load(f)
    for role_signature, role_body in roles.items():
        role_name, sep, role_args_str = role_signature.partition("/")
        role_args = role_args_str.split(",")
        role_yaml[role_name] = {"role_args": role_args, "role_body": role_body}

    return {
        role_name: parse_role(role_name, role_yaml, resources)
        for role_name in role_yaml.keys()
    }
