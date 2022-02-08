# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetOptionGroupResult',
    'AwaitableGetOptionGroupResult',
    'get_option_group',
    'get_option_group_output',
]

@pulumi.output_type
class GetOptionGroupResult:
    def __init__(__self__, id=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.OptionGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetOptionGroupResult(GetOptionGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOptionGroupResult(
            id=self.id,
            tags=self.tags)


def get_option_group(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOptionGroupResult:
    """
    Resource Type definition for AWS::RDS::OptionGroup
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:rds:getOptionGroup', __args__, opts=opts, typ=GetOptionGroupResult).value

    return AwaitableGetOptionGroupResult(
        id=__ret__.id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_option_group)
def get_option_group_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOptionGroupResult]:
    """
    Resource Type definition for AWS::RDS::OptionGroup
    """
    ...
