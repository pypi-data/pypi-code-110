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
    'GetFleetResult',
    'AwaitableGetFleetResult',
    'get_fleet',
    'get_fleet_output',
]

@pulumi.output_type
class GetFleetResult:
    def __init__(__self__, arn=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional['outputs.FleetTags']:
        return pulumi.get(self, "tags")


class AwaitableGetFleetResult(GetFleetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFleetResult(
            arn=self.arn,
            tags=self.tags)


def get_fleet(arn: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFleetResult:
    """
    AWS::RoboMaker::Fleet resource creates an AWS RoboMaker fleet. Fleets contain robots and can receive deployments.
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:robomaker:getFleet', __args__, opts=opts, typ=GetFleetResult).value

    return AwaitableGetFleetResult(
        arn=__ret__.arn,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_fleet)
def get_fleet_output(arn: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFleetResult]:
    """
    AWS::RoboMaker::Fleet resource creates an AWS RoboMaker fleet. Fleets contain robots and can receive deployments.
    """
    ...
