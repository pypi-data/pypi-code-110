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

__all__ = ['OriginRequestPolicyArgs', 'OriginRequestPolicy']

@pulumi.input_type
class OriginRequestPolicyArgs:
    def __init__(__self__, *,
                 origin_request_policy_config: pulumi.Input['OriginRequestPolicyConfigArgs']):
        """
        The set of arguments for constructing a OriginRequestPolicy resource.
        """
        pulumi.set(__self__, "origin_request_policy_config", origin_request_policy_config)

    @property
    @pulumi.getter(name="originRequestPolicyConfig")
    def origin_request_policy_config(self) -> pulumi.Input['OriginRequestPolicyConfigArgs']:
        return pulumi.get(self, "origin_request_policy_config")

    @origin_request_policy_config.setter
    def origin_request_policy_config(self, value: pulumi.Input['OriginRequestPolicyConfigArgs']):
        pulumi.set(self, "origin_request_policy_config", value)


class OriginRequestPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 origin_request_policy_config: Optional[pulumi.Input[pulumi.InputType['OriginRequestPolicyConfigArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CloudFront::OriginRequestPolicy

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OriginRequestPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CloudFront::OriginRequestPolicy

        :param str resource_name: The name of the resource.
        :param OriginRequestPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OriginRequestPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 origin_request_policy_config: Optional[pulumi.Input[pulumi.InputType['OriginRequestPolicyConfigArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OriginRequestPolicyArgs.__new__(OriginRequestPolicyArgs)

            if origin_request_policy_config is None and not opts.urn:
                raise TypeError("Missing required property 'origin_request_policy_config'")
            __props__.__dict__["origin_request_policy_config"] = origin_request_policy_config
            __props__.__dict__["last_modified_time"] = None
        super(OriginRequestPolicy, __self__).__init__(
            'aws-native:cloudfront:OriginRequestPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OriginRequestPolicy':
        """
        Get an existing OriginRequestPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OriginRequestPolicyArgs.__new__(OriginRequestPolicyArgs)

        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["origin_request_policy_config"] = None
        return OriginRequestPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="originRequestPolicyConfig")
    def origin_request_policy_config(self) -> pulumi.Output['outputs.OriginRequestPolicyConfig']:
        return pulumi.get(self, "origin_request_policy_config")

