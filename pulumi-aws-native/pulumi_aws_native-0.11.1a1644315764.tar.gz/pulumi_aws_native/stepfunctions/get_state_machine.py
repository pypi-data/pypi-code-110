# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetStateMachineResult',
    'AwaitableGetStateMachineResult',
    'get_state_machine',
    'get_state_machine_output',
]

@pulumi.output_type
class GetStateMachineResult:
    def __init__(__self__, arn=None, definition_string=None, logging_configuration=None, name=None, role_arn=None, state_machine_type=None, tags=None, tracing_configuration=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if definition_string and not isinstance(definition_string, str):
            raise TypeError("Expected argument 'definition_string' to be a str")
        pulumi.set(__self__, "definition_string", definition_string)
        if logging_configuration and not isinstance(logging_configuration, dict):
            raise TypeError("Expected argument 'logging_configuration' to be a dict")
        pulumi.set(__self__, "logging_configuration", logging_configuration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if role_arn and not isinstance(role_arn, str):
            raise TypeError("Expected argument 'role_arn' to be a str")
        pulumi.set(__self__, "role_arn", role_arn)
        if state_machine_type and not isinstance(state_machine_type, str):
            raise TypeError("Expected argument 'state_machine_type' to be a str")
        pulumi.set(__self__, "state_machine_type", state_machine_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tracing_configuration and not isinstance(tracing_configuration, dict):
            raise TypeError("Expected argument 'tracing_configuration' to be a dict")
        pulumi.set(__self__, "tracing_configuration", tracing_configuration)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="definitionString")
    def definition_string(self) -> Optional[str]:
        return pulumi.get(self, "definition_string")

    @property
    @pulumi.getter(name="loggingConfiguration")
    def logging_configuration(self) -> Optional['outputs.StateMachineLoggingConfiguration']:
        return pulumi.get(self, "logging_configuration")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="stateMachineType")
    def state_machine_type(self) -> Optional['StateMachineType']:
        return pulumi.get(self, "state_machine_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.StateMachineTagsEntry']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tracingConfiguration")
    def tracing_configuration(self) -> Optional['outputs.StateMachineTracingConfiguration']:
        return pulumi.get(self, "tracing_configuration")


class AwaitableGetStateMachineResult(GetStateMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStateMachineResult(
            arn=self.arn,
            definition_string=self.definition_string,
            logging_configuration=self.logging_configuration,
            name=self.name,
            role_arn=self.role_arn,
            state_machine_type=self.state_machine_type,
            tags=self.tags,
            tracing_configuration=self.tracing_configuration)


def get_state_machine(arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStateMachineResult:
    """
    Resource schema for StateMachine
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:stepfunctions:getStateMachine', __args__, opts=opts, typ=GetStateMachineResult).value

    return AwaitableGetStateMachineResult(
        arn=__ret__.arn,
        definition_string=__ret__.definition_string,
        logging_configuration=__ret__.logging_configuration,
        name=__ret__.name,
        role_arn=__ret__.role_arn,
        state_machine_type=__ret__.state_machine_type,
        tags=__ret__.tags,
        tracing_configuration=__ret__.tracing_configuration)


@_utilities.lift_output_func(get_state_machine)
def get_state_machine_output(arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStateMachineResult]:
    """
    Resource schema for StateMachine
    """
    ...
