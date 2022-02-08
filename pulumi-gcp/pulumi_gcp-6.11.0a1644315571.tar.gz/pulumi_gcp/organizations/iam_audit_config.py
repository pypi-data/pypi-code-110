# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['IamAuditConfigArgs', 'IamAuditConfig']

@pulumi.input_type
class IamAuditConfigArgs:
    def __init__(__self__, *,
                 audit_log_configs: pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]],
                 org_id: pulumi.Input[str],
                 service: pulumi.Input[str]):
        """
        The set of arguments for constructing a IamAuditConfig resource.
        :param pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]] audit_log_configs: The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
        :param pulumi.Input[str] org_id: The numeric ID of the organization in which you want to manage the audit logging config.
        :param pulumi.Input[str] service: Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_organization\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `log_types` specified in each `audit_log_config` are enabled, and the `exempted_members` in each `audit_log_config` are exempted.
        """
        pulumi.set(__self__, "audit_log_configs", audit_log_configs)
        pulumi.set(__self__, "org_id", org_id)
        pulumi.set(__self__, "service", service)

    @property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(self) -> pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]]:
        """
        The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
        """
        return pulumi.get(self, "audit_log_configs")

    @audit_log_configs.setter
    def audit_log_configs(self, value: pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]]):
        pulumi.set(self, "audit_log_configs", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[str]:
        """
        The numeric ID of the organization in which you want to manage the audit logging config.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def service(self) -> pulumi.Input[str]:
        """
        Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_organization\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `log_types` specified in each `audit_log_config` are enabled, and the `exempted_members` in each `audit_log_config` are exempted.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input[str]):
        pulumi.set(self, "service", value)


@pulumi.input_type
class _IamAuditConfigState:
    def __init__(__self__, *,
                 audit_log_configs: Optional[pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IamAuditConfig resources.
        :param pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]] audit_log_configs: The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
        :param pulumi.Input[str] etag: The etag of iam policy
        :param pulumi.Input[str] org_id: The numeric ID of the organization in which you want to manage the audit logging config.
        :param pulumi.Input[str] service: Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_organization\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `log_types` specified in each `audit_log_config` are enabled, and the `exempted_members` in each `audit_log_config` are exempted.
        """
        if audit_log_configs is not None:
            pulumi.set(__self__, "audit_log_configs", audit_log_configs)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if service is not None:
            pulumi.set(__self__, "service", service)

    @property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]]]:
        """
        The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
        """
        return pulumi.get(self, "audit_log_configs")

    @audit_log_configs.setter
    def audit_log_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IamAuditConfigAuditLogConfigArgs']]]]):
        pulumi.set(self, "audit_log_configs", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        The etag of iam policy
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        The numeric ID of the organization in which you want to manage the audit logging config.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[str]]:
        """
        Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_organization\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `log_types` specified in each `audit_log_config` are enabled, and the `exempted_members` in each `audit_log_config` are exempted.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service", value)


class IamAuditConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_log_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IamAuditConfigAuditLogConfigArgs']]]]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Allows management of audit logging config for a given service for a Google Cloud Platform Organization.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        config = gcp.organizations.IamAuditConfig("config",
            audit_log_configs=[gcp.organizations.IamAuditConfigAuditLogConfigArgs(
                exempted_members=["user:joebloggs@hashicorp.com"],
                log_type="DATA_READ",
            )],
            org_id="your-organization-id",
            service="allServices")
        ```

        ## Import

        IAM audit config imports use the identifier of the resource in question and the service, e.g.

        ```sh
         $ pulumi import gcp:organizations/iamAuditConfig:IamAuditConfig config "your-organization-id foo.googleapis.com"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IamAuditConfigAuditLogConfigArgs']]]] audit_log_configs: The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
        :param pulumi.Input[str] org_id: The numeric ID of the organization in which you want to manage the audit logging config.
        :param pulumi.Input[str] service: Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_organization\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `log_types` specified in each `audit_log_config` are enabled, and the `exempted_members` in each `audit_log_config` are exempted.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IamAuditConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows management of audit logging config for a given service for a Google Cloud Platform Organization.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gcp as gcp

        config = gcp.organizations.IamAuditConfig("config",
            audit_log_configs=[gcp.organizations.IamAuditConfigAuditLogConfigArgs(
                exempted_members=["user:joebloggs@hashicorp.com"],
                log_type="DATA_READ",
            )],
            org_id="your-organization-id",
            service="allServices")
        ```

        ## Import

        IAM audit config imports use the identifier of the resource in question and the service, e.g.

        ```sh
         $ pulumi import gcp:organizations/iamAuditConfig:IamAuditConfig config "your-organization-id foo.googleapis.com"
        ```

        :param str resource_name: The name of the resource.
        :param IamAuditConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IamAuditConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_log_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IamAuditConfigAuditLogConfigArgs']]]]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
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
            __props__ = IamAuditConfigArgs.__new__(IamAuditConfigArgs)

            if audit_log_configs is None and not opts.urn:
                raise TypeError("Missing required property 'audit_log_configs'")
            __props__.__dict__["audit_log_configs"] = audit_log_configs
            if org_id is None and not opts.urn:
                raise TypeError("Missing required property 'org_id'")
            __props__.__dict__["org_id"] = org_id
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__.__dict__["service"] = service
            __props__.__dict__["etag"] = None
        super(IamAuditConfig, __self__).__init__(
            'gcp:organizations/iamAuditConfig:IamAuditConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            audit_log_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IamAuditConfigAuditLogConfigArgs']]]]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            service: Optional[pulumi.Input[str]] = None) -> 'IamAuditConfig':
        """
        Get an existing IamAuditConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IamAuditConfigAuditLogConfigArgs']]]] audit_log_configs: The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
        :param pulumi.Input[str] etag: The etag of iam policy
        :param pulumi.Input[str] org_id: The numeric ID of the organization in which you want to manage the audit logging config.
        :param pulumi.Input[str] service: Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_organization\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `log_types` specified in each `audit_log_config` are enabled, and the `exempted_members` in each `audit_log_config` are exempted.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IamAuditConfigState.__new__(_IamAuditConfigState)

        __props__.__dict__["audit_log_configs"] = audit_log_configs
        __props__.__dict__["etag"] = etag
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["service"] = service
        return IamAuditConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(self) -> pulumi.Output[Sequence['outputs.IamAuditConfigAuditLogConfig']]:
        """
        The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.
        """
        return pulumi.get(self, "audit_log_configs")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The etag of iam policy
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        """
        The numeric ID of the organization in which you want to manage the audit logging config.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        Service which will be enabled for audit logging.  The special value `allServices` covers all services.  Note that if there are google\_organization\_iam\_audit\_config resources covering both `allServices` and a specific service then the union of the two AuditConfigs is used for that service: the `log_types` specified in each `audit_log_config` are enabled, and the `exempted_members` in each `audit_log_config` are exempted.
        """
        return pulumi.get(self, "service")

