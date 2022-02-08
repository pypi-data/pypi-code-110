# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetUserHierarchyGroupResult',
    'AwaitableGetUserHierarchyGroupResult',
    'get_user_hierarchy_group',
    'get_user_hierarchy_group_output',
]

@pulumi.output_type
class GetUserHierarchyGroupResult:
    def __init__(__self__, instance_arn=None, name=None, user_hierarchy_group_arn=None):
        if instance_arn and not isinstance(instance_arn, str):
            raise TypeError("Expected argument 'instance_arn' to be a str")
        pulumi.set(__self__, "instance_arn", instance_arn)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if user_hierarchy_group_arn and not isinstance(user_hierarchy_group_arn, str):
            raise TypeError("Expected argument 'user_hierarchy_group_arn' to be a str")
        pulumi.set(__self__, "user_hierarchy_group_arn", user_hierarchy_group_arn)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the user hierarchy group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="userHierarchyGroupArn")
    def user_hierarchy_group_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the user hierarchy group.
        """
        return pulumi.get(self, "user_hierarchy_group_arn")


class AwaitableGetUserHierarchyGroupResult(GetUserHierarchyGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserHierarchyGroupResult(
            instance_arn=self.instance_arn,
            name=self.name,
            user_hierarchy_group_arn=self.user_hierarchy_group_arn)


def get_user_hierarchy_group(user_hierarchy_group_arn: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserHierarchyGroupResult:
    """
    Resource Type definition for AWS::Connect::UserHierarchyGroup


    :param str user_hierarchy_group_arn: The Amazon Resource Name (ARN) for the user hierarchy group.
    """
    __args__ = dict()
    __args__['userHierarchyGroupArn'] = user_hierarchy_group_arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getUserHierarchyGroup', __args__, opts=opts, typ=GetUserHierarchyGroupResult).value

    return AwaitableGetUserHierarchyGroupResult(
        instance_arn=__ret__.instance_arn,
        name=__ret__.name,
        user_hierarchy_group_arn=__ret__.user_hierarchy_group_arn)


@_utilities.lift_output_func(get_user_hierarchy_group)
def get_user_hierarchy_group_output(user_hierarchy_group_arn: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserHierarchyGroupResult]:
    """
    Resource Type definition for AWS::Connect::UserHierarchyGroup


    :param str user_hierarchy_group_arn: The Amazon Resource Name (ARN) for the user hierarchy group.
    """
    ...
