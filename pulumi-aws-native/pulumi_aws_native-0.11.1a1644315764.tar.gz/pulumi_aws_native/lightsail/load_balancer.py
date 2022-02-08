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

__all__ = ['LoadBalancerArgs', 'LoadBalancer']

@pulumi.input_type
class LoadBalancerArgs:
    def __init__(__self__, *,
                 instance_port: pulumi.Input[int],
                 attached_instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 ip_address_type: Optional[pulumi.Input[str]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 session_stickiness_enabled: Optional[pulumi.Input[bool]] = None,
                 session_stickiness_lb_cookie_duration_seconds: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerTagArgs']]]] = None):
        """
        The set of arguments for constructing a LoadBalancer resource.
        :param pulumi.Input[int] instance_port: The instance port where you're creating your load balancer.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_instances: The names of the instances attached to the load balancer.
        :param pulumi.Input[str] health_check_path: The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "/").
        :param pulumi.Input[str] ip_address_type: The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. The default value is dualstack.
        :param pulumi.Input[str] load_balancer_name: The name of your load balancer.
        :param pulumi.Input[bool] session_stickiness_enabled: Configuration option to enable session stickiness.
        :param pulumi.Input[str] session_stickiness_lb_cookie_duration_seconds: Configuration option to adjust session stickiness cookie duration parameter.
        :param pulumi.Input[Sequence[pulumi.Input['LoadBalancerTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "instance_port", instance_port)
        if attached_instances is not None:
            pulumi.set(__self__, "attached_instances", attached_instances)
        if health_check_path is not None:
            pulumi.set(__self__, "health_check_path", health_check_path)
        if ip_address_type is not None:
            pulumi.set(__self__, "ip_address_type", ip_address_type)
        if load_balancer_name is not None:
            pulumi.set(__self__, "load_balancer_name", load_balancer_name)
        if session_stickiness_enabled is not None:
            pulumi.set(__self__, "session_stickiness_enabled", session_stickiness_enabled)
        if session_stickiness_lb_cookie_duration_seconds is not None:
            pulumi.set(__self__, "session_stickiness_lb_cookie_duration_seconds", session_stickiness_lb_cookie_duration_seconds)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> pulumi.Input[int]:
        """
        The instance port where you're creating your load balancer.
        """
        return pulumi.get(self, "instance_port")

    @instance_port.setter
    def instance_port(self, value: pulumi.Input[int]):
        pulumi.set(self, "instance_port", value)

    @property
    @pulumi.getter(name="attachedInstances")
    def attached_instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The names of the instances attached to the load balancer.
        """
        return pulumi.get(self, "attached_instances")

    @attached_instances.setter
    def attached_instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attached_instances", value)

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "/").
        """
        return pulumi.get(self, "health_check_path")

    @health_check_path.setter
    def health_check_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "health_check_path", value)

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. The default value is dualstack.
        """
        return pulumi.get(self, "ip_address_type")

    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address_type", value)

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of your load balancer.
        """
        return pulumi.get(self, "load_balancer_name")

    @load_balancer_name.setter
    def load_balancer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "load_balancer_name", value)

    @property
    @pulumi.getter(name="sessionStickinessEnabled")
    def session_stickiness_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Configuration option to enable session stickiness.
        """
        return pulumi.get(self, "session_stickiness_enabled")

    @session_stickiness_enabled.setter
    def session_stickiness_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "session_stickiness_enabled", value)

    @property
    @pulumi.getter(name="sessionStickinessLBCookieDurationSeconds")
    def session_stickiness_lb_cookie_duration_seconds(self) -> Optional[pulumi.Input[str]]:
        """
        Configuration option to adjust session stickiness cookie duration parameter.
        """
        return pulumi.get(self, "session_stickiness_lb_cookie_duration_seconds")

    @session_stickiness_lb_cookie_duration_seconds.setter
    def session_stickiness_lb_cookie_duration_seconds(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_stickiness_lb_cookie_duration_seconds", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LoadBalancerTagArgs']]]]):
        pulumi.set(self, "tags", value)


class LoadBalancer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 instance_port: Optional[pulumi.Input[int]] = None,
                 ip_address_type: Optional[pulumi.Input[str]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 session_stickiness_enabled: Optional[pulumi.Input[bool]] = None,
                 session_stickiness_lb_cookie_duration_seconds: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Lightsail::LoadBalancer

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] attached_instances: The names of the instances attached to the load balancer.
        :param pulumi.Input[str] health_check_path: The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "/").
        :param pulumi.Input[int] instance_port: The instance port where you're creating your load balancer.
        :param pulumi.Input[str] ip_address_type: The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. The default value is dualstack.
        :param pulumi.Input[str] load_balancer_name: The name of your load balancer.
        :param pulumi.Input[bool] session_stickiness_enabled: Configuration option to enable session stickiness.
        :param pulumi.Input[str] session_stickiness_lb_cookie_duration_seconds: Configuration option to adjust session stickiness cookie duration parameter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoadBalancerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Lightsail::LoadBalancer

        :param str resource_name: The name of the resource.
        :param LoadBalancerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoadBalancerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 health_check_path: Optional[pulumi.Input[str]] = None,
                 instance_port: Optional[pulumi.Input[int]] = None,
                 ip_address_type: Optional[pulumi.Input[str]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 session_stickiness_enabled: Optional[pulumi.Input[bool]] = None,
                 session_stickiness_lb_cookie_duration_seconds: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LoadBalancerTagArgs']]]]] = None,
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
            __props__ = LoadBalancerArgs.__new__(LoadBalancerArgs)

            __props__.__dict__["attached_instances"] = attached_instances
            __props__.__dict__["health_check_path"] = health_check_path
            if instance_port is None and not opts.urn:
                raise TypeError("Missing required property 'instance_port'")
            __props__.__dict__["instance_port"] = instance_port
            __props__.__dict__["ip_address_type"] = ip_address_type
            __props__.__dict__["load_balancer_name"] = load_balancer_name
            __props__.__dict__["session_stickiness_enabled"] = session_stickiness_enabled
            __props__.__dict__["session_stickiness_lb_cookie_duration_seconds"] = session_stickiness_lb_cookie_duration_seconds
            __props__.__dict__["tags"] = tags
            __props__.__dict__["load_balancer_arn"] = None
        super(LoadBalancer, __self__).__init__(
            'aws-native:lightsail:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LoadBalancer':
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LoadBalancerArgs.__new__(LoadBalancerArgs)

        __props__.__dict__["attached_instances"] = None
        __props__.__dict__["health_check_path"] = None
        __props__.__dict__["instance_port"] = None
        __props__.__dict__["ip_address_type"] = None
        __props__.__dict__["load_balancer_arn"] = None
        __props__.__dict__["load_balancer_name"] = None
        __props__.__dict__["session_stickiness_enabled"] = None
        __props__.__dict__["session_stickiness_lb_cookie_duration_seconds"] = None
        __props__.__dict__["tags"] = None
        return LoadBalancer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachedInstances")
    def attached_instances(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The names of the instances attached to the load balancer.
        """
        return pulumi.get(self, "attached_instances")

    @property
    @pulumi.getter(name="healthCheckPath")
    def health_check_path(self) -> pulumi.Output[Optional[str]]:
        """
        The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., "/").
        """
        return pulumi.get(self, "health_check_path")

    @property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> pulumi.Output[int]:
        """
        The instance port where you're creating your load balancer.
        """
        return pulumi.get(self, "instance_port")

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[Optional[str]]:
        """
        The IP address type for the load balancer. The possible values are ipv4 for IPv4 only, and dualstack for IPv4 and IPv6. The default value is dualstack.
        """
        return pulumi.get(self, "ip_address_type")

    @property
    @pulumi.getter(name="loadBalancerArn")
    def load_balancer_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "load_balancer_arn")

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> pulumi.Output[str]:
        """
        The name of your load balancer.
        """
        return pulumi.get(self, "load_balancer_name")

    @property
    @pulumi.getter(name="sessionStickinessEnabled")
    def session_stickiness_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Configuration option to enable session stickiness.
        """
        return pulumi.get(self, "session_stickiness_enabled")

    @property
    @pulumi.getter(name="sessionStickinessLBCookieDurationSeconds")
    def session_stickiness_lb_cookie_duration_seconds(self) -> pulumi.Output[Optional[str]]:
        """
        Configuration option to adjust session stickiness cookie duration parameter.
        """
        return pulumi.get(self, "session_stickiness_lb_cookie_duration_seconds")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.LoadBalancerTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

