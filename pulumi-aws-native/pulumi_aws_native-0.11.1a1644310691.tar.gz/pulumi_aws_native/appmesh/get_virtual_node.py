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
    'GetVirtualNodeResult',
    'AwaitableGetVirtualNodeResult',
    'get_virtual_node',
    'get_virtual_node_output',
]

@pulumi.output_type
class GetVirtualNodeResult:
    def __init__(__self__, arn=None, id=None, resource_owner=None, spec=None, tags=None, uid=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource_owner and not isinstance(resource_owner, str):
            raise TypeError("Expected argument 'resource_owner' to be a str")
        pulumi.set(__self__, "resource_owner", resource_owner)
        if spec and not isinstance(spec, dict):
            raise TypeError("Expected argument 'spec' to be a dict")
        pulumi.set(__self__, "spec", spec)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> Optional[str]:
        return pulumi.get(self, "resource_owner")

    @property
    @pulumi.getter
    def spec(self) -> Optional['outputs.VirtualNodeSpec']:
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.VirtualNodeTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def uid(self) -> Optional[str]:
        return pulumi.get(self, "uid")


class AwaitableGetVirtualNodeResult(GetVirtualNodeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualNodeResult(
            arn=self.arn,
            id=self.id,
            resource_owner=self.resource_owner,
            spec=self.spec,
            tags=self.tags,
            uid=self.uid)


def get_virtual_node(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualNodeResult:
    """
    Resource Type definition for AWS::AppMesh::VirtualNode
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:appmesh:getVirtualNode', __args__, opts=opts, typ=GetVirtualNodeResult).value

    return AwaitableGetVirtualNodeResult(
        arn=__ret__.arn,
        id=__ret__.id,
        resource_owner=__ret__.resource_owner,
        spec=__ret__.spec,
        tags=__ret__.tags,
        uid=__ret__.uid)


@_utilities.lift_output_func(get_virtual_node)
def get_virtual_node_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualNodeResult]:
    """
    Resource Type definition for AWS::AppMesh::VirtualNode
    """
    ...
