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
from ._inputs import *

__all__ = ['ApplicationInstanceArgs', 'ApplicationInstance']

@pulumi.input_type
class ApplicationInstanceArgs:
    def __init__(__self__, *,
                 default_runtime_context_device: pulumi.Input[str],
                 manifest_payload: pulumi.Input['ApplicationInstanceManifestPayloadArgs'],
                 application_instance_id_to_replace: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[str]] = None,
                 manifest_overrides_payload: Optional[pulumi.Input['ApplicationInstanceManifestOverridesPayloadArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 runtime_role_arn: Optional[pulumi.Input[str]] = None,
                 status_filter: Optional[pulumi.Input['ApplicationInstanceStatusFilter']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationInstanceTagArgs']]]] = None):
        """
        The set of arguments for constructing a ApplicationInstance resource.
        """
        pulumi.set(__self__, "default_runtime_context_device", default_runtime_context_device)
        pulumi.set(__self__, "manifest_payload", manifest_payload)
        if application_instance_id_to_replace is not None:
            pulumi.set(__self__, "application_instance_id_to_replace", application_instance_id_to_replace)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if manifest_overrides_payload is not None:
            pulumi.set(__self__, "manifest_overrides_payload", manifest_overrides_payload)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if runtime_role_arn is not None:
            pulumi.set(__self__, "runtime_role_arn", runtime_role_arn)
        if status_filter is not None:
            pulumi.set(__self__, "status_filter", status_filter)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="defaultRuntimeContextDevice")
    def default_runtime_context_device(self) -> pulumi.Input[str]:
        return pulumi.get(self, "default_runtime_context_device")

    @default_runtime_context_device.setter
    def default_runtime_context_device(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_runtime_context_device", value)

    @property
    @pulumi.getter(name="manifestPayload")
    def manifest_payload(self) -> pulumi.Input['ApplicationInstanceManifestPayloadArgs']:
        return pulumi.get(self, "manifest_payload")

    @manifest_payload.setter
    def manifest_payload(self, value: pulumi.Input['ApplicationInstanceManifestPayloadArgs']):
        pulumi.set(self, "manifest_payload", value)

    @property
    @pulumi.getter(name="applicationInstanceIdToReplace")
    def application_instance_id_to_replace(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "application_instance_id_to_replace")

    @application_instance_id_to_replace.setter
    def application_instance_id_to_replace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_instance_id_to_replace", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "device_id")

    @device_id.setter
    def device_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_id", value)

    @property
    @pulumi.getter(name="manifestOverridesPayload")
    def manifest_overrides_payload(self) -> Optional[pulumi.Input['ApplicationInstanceManifestOverridesPayloadArgs']]:
        return pulumi.get(self, "manifest_overrides_payload")

    @manifest_overrides_payload.setter
    def manifest_overrides_payload(self, value: Optional[pulumi.Input['ApplicationInstanceManifestOverridesPayloadArgs']]):
        pulumi.set(self, "manifest_overrides_payload", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="runtimeRoleArn")
    def runtime_role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "runtime_role_arn")

    @runtime_role_arn.setter
    def runtime_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "runtime_role_arn", value)

    @property
    @pulumi.getter(name="statusFilter")
    def status_filter(self) -> Optional[pulumi.Input['ApplicationInstanceStatusFilter']]:
        return pulumi.get(self, "status_filter")

    @status_filter.setter
    def status_filter(self, value: Optional[pulumi.Input['ApplicationInstanceStatusFilter']]):
        pulumi.set(self, "status_filter", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationInstanceTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationInstanceTagArgs']]]]):
        pulumi.set(self, "tags", value)


class ApplicationInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_instance_id_to_replace: Optional[pulumi.Input[str]] = None,
                 default_runtime_context_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[str]] = None,
                 manifest_overrides_payload: Optional[pulumi.Input[pulumi.InputType['ApplicationInstanceManifestOverridesPayloadArgs']]] = None,
                 manifest_payload: Optional[pulumi.Input[pulumi.InputType['ApplicationInstanceManifestPayloadArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 runtime_role_arn: Optional[pulumi.Input[str]] = None,
                 status_filter: Optional[pulumi.Input['ApplicationInstanceStatusFilter']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationInstanceTagArgs']]]]] = None,
                 __props__=None):
        """
        Schema for ApplicationInstance CloudFormation Resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema for ApplicationInstance CloudFormation Resource

        :param str resource_name: The name of the resource.
        :param ApplicationInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_instance_id_to_replace: Optional[pulumi.Input[str]] = None,
                 default_runtime_context_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[str]] = None,
                 manifest_overrides_payload: Optional[pulumi.Input[pulumi.InputType['ApplicationInstanceManifestOverridesPayloadArgs']]] = None,
                 manifest_payload: Optional[pulumi.Input[pulumi.InputType['ApplicationInstanceManifestPayloadArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 runtime_role_arn: Optional[pulumi.Input[str]] = None,
                 status_filter: Optional[pulumi.Input['ApplicationInstanceStatusFilter']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationInstanceTagArgs']]]]] = None,
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
            __props__ = ApplicationInstanceArgs.__new__(ApplicationInstanceArgs)

            __props__.__dict__["application_instance_id_to_replace"] = application_instance_id_to_replace
            if default_runtime_context_device is None and not opts.urn:
                raise TypeError("Missing required property 'default_runtime_context_device'")
            __props__.__dict__["default_runtime_context_device"] = default_runtime_context_device
            __props__.__dict__["description"] = description
            __props__.__dict__["device_id"] = device_id
            __props__.__dict__["manifest_overrides_payload"] = manifest_overrides_payload
            if manifest_payload is None and not opts.urn:
                raise TypeError("Missing required property 'manifest_payload'")
            __props__.__dict__["manifest_payload"] = manifest_payload
            __props__.__dict__["name"] = name
            __props__.__dict__["runtime_role_arn"] = runtime_role_arn
            __props__.__dict__["status_filter"] = status_filter
            __props__.__dict__["tags"] = tags
            __props__.__dict__["application_instance_id"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["default_runtime_context_device_name"] = None
            __props__.__dict__["health_status"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_description"] = None
        super(ApplicationInstance, __self__).__init__(
            'aws-native:panorama:ApplicationInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationInstance':
        """
        Get an existing ApplicationInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationInstanceArgs.__new__(ApplicationInstanceArgs)

        __props__.__dict__["application_instance_id"] = None
        __props__.__dict__["application_instance_id_to_replace"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["default_runtime_context_device"] = None
        __props__.__dict__["default_runtime_context_device_name"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["device_id"] = None
        __props__.__dict__["health_status"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["manifest_overrides_payload"] = None
        __props__.__dict__["manifest_payload"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["runtime_role_arn"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_description"] = None
        __props__.__dict__["status_filter"] = None
        __props__.__dict__["tags"] = None
        return ApplicationInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationInstanceId")
    def application_instance_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_instance_id")

    @property
    @pulumi.getter(name="applicationInstanceIdToReplace")
    def application_instance_id_to_replace(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "application_instance_id_to_replace")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[int]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="defaultRuntimeContextDevice")
    def default_runtime_context_device(self) -> pulumi.Output[str]:
        return pulumi.get(self, "default_runtime_context_device")

    @property
    @pulumi.getter(name="defaultRuntimeContextDeviceName")
    def default_runtime_context_device_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "default_runtime_context_device_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> pulumi.Output['ApplicationInstanceHealthStatus']:
        return pulumi.get(self, "health_status")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[int]:
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="manifestOverridesPayload")
    def manifest_overrides_payload(self) -> pulumi.Output[Optional['outputs.ApplicationInstanceManifestOverridesPayload']]:
        return pulumi.get(self, "manifest_overrides_payload")

    @property
    @pulumi.getter(name="manifestPayload")
    def manifest_payload(self) -> pulumi.Output['outputs.ApplicationInstanceManifestPayload']:
        return pulumi.get(self, "manifest_payload")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="runtimeRoleArn")
    def runtime_role_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "runtime_role_arn")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['ApplicationInstanceStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusDescription")
    def status_description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status_description")

    @property
    @pulumi.getter(name="statusFilter")
    def status_filter(self) -> pulumi.Output[Optional['ApplicationInstanceStatusFilter']]:
        return pulumi.get(self, "status_filter")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationInstanceTag']]]:
        return pulumi.get(self, "tags")

