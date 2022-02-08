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
    'GetLocationEFSResult',
    'AwaitableGetLocationEFSResult',
    'get_location_efs',
    'get_location_efs_output',
]

@pulumi.output_type
class GetLocationEFSResult:
    def __init__(__self__, location_arn=None, location_uri=None, tags=None):
        if location_arn and not isinstance(location_arn, str):
            raise TypeError("Expected argument 'location_arn' to be a str")
        pulumi.set(__self__, "location_arn", location_arn)
        if location_uri and not isinstance(location_uri, str):
            raise TypeError("Expected argument 'location_uri' to be a str")
        pulumi.set(__self__, "location_uri", location_uri)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[str]:
        """
        The URL of the EFS location that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.LocationEFSTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLocationEFSResult(GetLocationEFSResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocationEFSResult(
            location_arn=self.location_arn,
            location_uri=self.location_uri,
            tags=self.tags)


def get_location_efs(location_arn: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocationEFSResult:
    """
    Resource schema for AWS::DataSync::LocationEFS.


    :param str location_arn: The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
    """
    __args__ = dict()
    __args__['locationArn'] = location_arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:datasync:getLocationEFS', __args__, opts=opts, typ=GetLocationEFSResult).value

    return AwaitableGetLocationEFSResult(
        location_arn=__ret__.location_arn,
        location_uri=__ret__.location_uri,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_location_efs)
def get_location_efs_output(location_arn: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocationEFSResult]:
    """
    Resource schema for AWS::DataSync::LocationEFS.


    :param str location_arn: The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
    """
    ...
