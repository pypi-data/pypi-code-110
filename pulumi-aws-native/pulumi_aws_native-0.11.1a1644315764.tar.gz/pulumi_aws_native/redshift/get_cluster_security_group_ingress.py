# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetClusterSecurityGroupIngressResult',
    'AwaitableGetClusterSecurityGroupIngressResult',
    'get_cluster_security_group_ingress',
    'get_cluster_security_group_ingress_output',
]

@pulumi.output_type
class GetClusterSecurityGroupIngressResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetClusterSecurityGroupIngressResult(GetClusterSecurityGroupIngressResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterSecurityGroupIngressResult(
            id=self.id)


def get_cluster_security_group_ingress(id: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterSecurityGroupIngressResult:
    """
    Resource Type definition for AWS::Redshift::ClusterSecurityGroupIngress
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:redshift:getClusterSecurityGroupIngress', __args__, opts=opts, typ=GetClusterSecurityGroupIngressResult).value

    return AwaitableGetClusterSecurityGroupIngressResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_cluster_security_group_ingress)
def get_cluster_security_group_ingress_output(id: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterSecurityGroupIngressResult]:
    """
    Resource Type definition for AWS::Redshift::ClusterSecurityGroupIngress
    """
    ...
