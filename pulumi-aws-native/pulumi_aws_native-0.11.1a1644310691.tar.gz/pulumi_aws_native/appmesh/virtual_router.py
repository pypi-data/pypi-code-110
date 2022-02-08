# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['VirtualRouterArgs', 'VirtualRouter']

@pulumi.input_type
class VirtualRouterArgs:
    def __init__(__self__, *,
                 mesh_name: pulumi.Input[str],
                 spec: pulumi.Input['VirtualRouterSpecArgs'],
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualRouterTagArgs']]]] = None,
                 virtual_router_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualRouter resource.
        """
        pulumi.set(__self__, "mesh_name", mesh_name)
        pulumi.set(__self__, "spec", spec)
        if mesh_owner is not None:
            pulumi.set(__self__, "mesh_owner", mesh_owner)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_router_name is not None:
            pulumi.set(__self__, "virtual_router_name", virtual_router_name)

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mesh_name")

    @mesh_name.setter
    def mesh_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mesh_name", value)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input['VirtualRouterSpecArgs']:
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input['VirtualRouterSpecArgs']):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mesh_owner")

    @mesh_owner.setter
    def mesh_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mesh_owner", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualRouterTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualRouterTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "virtual_router_name")

    @virtual_router_name.setter
    def virtual_router_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_router_name", value)


warnings.warn("""VirtualRouter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class VirtualRouter(pulumi.CustomResource):
    warnings.warn("""VirtualRouter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['VirtualRouterSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualRouterTagArgs']]]]] = None,
                 virtual_router_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppMesh::VirtualRouter

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualRouterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppMesh::VirtualRouter

        :param str resource_name: The name of the resource.
        :param VirtualRouterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualRouterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['VirtualRouterSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VirtualRouterTagArgs']]]]] = None,
                 virtual_router_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""VirtualRouter is deprecated: VirtualRouter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualRouterArgs.__new__(VirtualRouterArgs)

            if mesh_name is None and not opts.urn:
                raise TypeError("Missing required property 'mesh_name'")
            __props__.__dict__["mesh_name"] = mesh_name
            __props__.__dict__["mesh_owner"] = mesh_owner
            if spec is None and not opts.urn:
                raise TypeError("Missing required property 'spec'")
            __props__.__dict__["spec"] = spec
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_router_name"] = virtual_router_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["resource_owner"] = None
            __props__.__dict__["uid"] = None
        super(VirtualRouter, __self__).__init__(
            'aws-native:appmesh:VirtualRouter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualRouter':
        """
        Get an existing VirtualRouter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualRouterArgs.__new__(VirtualRouterArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["mesh_name"] = None
        __props__.__dict__["mesh_owner"] = None
        __props__.__dict__["resource_owner"] = None
        __props__.__dict__["spec"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["uid"] = None
        __props__.__dict__["virtual_router_name"] = None
        return VirtualRouter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "mesh_name")

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "mesh_owner")

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> pulumi.Output[str]:
        return pulumi.get(self, "resource_owner")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.VirtualRouterSpec']:
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VirtualRouterTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "virtual_router_name")

