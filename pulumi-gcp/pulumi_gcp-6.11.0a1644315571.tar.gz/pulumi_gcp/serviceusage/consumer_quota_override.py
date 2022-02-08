# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ConsumerQuotaOverrideArgs', 'ConsumerQuotaOverride']

@pulumi.input_type
class ConsumerQuotaOverrideArgs:
    def __init__(__self__, *,
                 limit: pulumi.Input[str],
                 metric: pulumi.Input[str],
                 override_value: pulumi.Input[str],
                 service: pulumi.Input[str],
                 dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConsumerQuotaOverride resource.
        :param pulumi.Input[str] limit: The limit on the metric, e.g. `/project/region`.
        :param pulumi.Input[str] metric: The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
        :param pulumi.Input[str] override_value: The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
        :param pulumi.Input[str] service: The service that the metrics belong to, e.g. `compute.googleapis.com`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] dimensions: If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
        :param pulumi.Input[bool] force: If the new quota would decrease the existing quota by more than 10%, the request is rejected.
               If `force` is `true`, that safety check is ignored.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "limit", limit)
        pulumi.set(__self__, "metric", metric)
        pulumi.set(__self__, "override_value", override_value)
        pulumi.set(__self__, "service", service)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def limit(self) -> pulumi.Input[str]:
        """
        The limit on the metric, e.g. `/project/region`.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: pulumi.Input[str]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def metric(self) -> pulumi.Input[str]:
        """
        The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
        """
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric", value)

    @property
    @pulumi.getter(name="overrideValue")
    def override_value(self) -> pulumi.Input[str]:
        """
        The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
        """
        return pulumi.get(self, "override_value")

    @override_value.setter
    def override_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "override_value", value)

    @property
    @pulumi.getter
    def service(self) -> pulumi.Input[str]:
        """
        The service that the metrics belong to, e.g. `compute.googleapis.com`.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: pulumi.Input[str]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        If the new quota would decrease the existing quota by more than 10%, the request is rejected.
        If `force` is `true`, that safety check is ignored.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _ConsumerQuotaOverrideState:
    def __init__(__self__, *,
                 dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 limit: Optional[pulumi.Input[str]] = None,
                 metric: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 override_value: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConsumerQuotaOverride resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] dimensions: If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
        :param pulumi.Input[bool] force: If the new quota would decrease the existing quota by more than 10%, the request is rejected.
               If `force` is `true`, that safety check is ignored.
        :param pulumi.Input[str] limit: The limit on the metric, e.g. `/project/region`.
        :param pulumi.Input[str] metric: The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
        :param pulumi.Input[str] name: The server-generated name of the quota override.
        :param pulumi.Input[str] override_value: The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The service that the metrics belong to, e.g. `compute.googleapis.com`.
        """
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if limit is not None:
            pulumi.set(__self__, "limit", limit)
        if metric is not None:
            pulumi.set(__self__, "metric", metric)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if override_value is not None:
            pulumi.set(__self__, "override_value", override_value)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if service is not None:
            pulumi.set(__self__, "service", service)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        If the new quota would decrease the existing quota by more than 10%, the request is rejected.
        If `force` is `true`, that safety check is ignored.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[str]]:
        """
        The limit on the metric, e.g. `/project/region`.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input[str]]:
        """
        The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
        """
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The server-generated name of the quota override.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="overrideValue")
    def override_value(self) -> Optional[pulumi.Input[str]]:
        """
        The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
        """
        return pulumi.get(self, "override_value")

    @override_value.setter
    def override_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "override_value", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[str]]:
        """
        The service that the metrics belong to, e.g. `compute.googleapis.com`.
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service", value)


class ConsumerQuotaOverride(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 limit: Optional[pulumi.Input[str]] = None,
                 metric: Optional[pulumi.Input[str]] = None,
                 override_value: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A consumer override is applied to the consumer on its own authority to limit its own quota usage.
        Consumer overrides cannot be used to grant more quota than would be allowed by admin overrides,
        producer overrides, or the default limit of the service.

        To get more information about ConsumerQuotaOverride, see:

        * How-to Guides
            * [Getting Started](https://cloud.google.com/service-usage/docs/getting-started)
            * [REST API documentation](https://cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides)

        ## Example Usage

        ## Import

        ConsumerQuotaOverride can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride default projects/{{project}}/services/{{service}}/consumerQuotaMetrics/{{metric}}/limits/{{limit}}/consumerOverrides/{{name}}
        ```

        ```sh
         $ pulumi import gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride default services/{{service}}/consumerQuotaMetrics/{{metric}}/limits/{{limit}}/consumerOverrides/{{name}}
        ```

        ```sh
         $ pulumi import gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride default {{service}}/{{metric}}/{{limit}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] dimensions: If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
        :param pulumi.Input[bool] force: If the new quota would decrease the existing quota by more than 10%, the request is rejected.
               If `force` is `true`, that safety check is ignored.
        :param pulumi.Input[str] limit: The limit on the metric, e.g. `/project/region`.
        :param pulumi.Input[str] metric: The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
        :param pulumi.Input[str] override_value: The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The service that the metrics belong to, e.g. `compute.googleapis.com`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConsumerQuotaOverrideArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A consumer override is applied to the consumer on its own authority to limit its own quota usage.
        Consumer overrides cannot be used to grant more quota than would be allowed by admin overrides,
        producer overrides, or the default limit of the service.

        To get more information about ConsumerQuotaOverride, see:

        * How-to Guides
            * [Getting Started](https://cloud.google.com/service-usage/docs/getting-started)
            * [REST API documentation](https://cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides)

        ## Example Usage

        ## Import

        ConsumerQuotaOverride can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride default projects/{{project}}/services/{{service}}/consumerQuotaMetrics/{{metric}}/limits/{{limit}}/consumerOverrides/{{name}}
        ```

        ```sh
         $ pulumi import gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride default services/{{service}}/consumerQuotaMetrics/{{metric}}/limits/{{limit}}/consumerOverrides/{{name}}
        ```

        ```sh
         $ pulumi import gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride default {{service}}/{{metric}}/{{limit}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param ConsumerQuotaOverrideArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConsumerQuotaOverrideArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 limit: Optional[pulumi.Input[str]] = None,
                 metric: Optional[pulumi.Input[str]] = None,
                 override_value: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = ConsumerQuotaOverrideArgs.__new__(ConsumerQuotaOverrideArgs)

            __props__.__dict__["dimensions"] = dimensions
            __props__.__dict__["force"] = force
            if limit is None and not opts.urn:
                raise TypeError("Missing required property 'limit'")
            __props__.__dict__["limit"] = limit
            if metric is None and not opts.urn:
                raise TypeError("Missing required property 'metric'")
            __props__.__dict__["metric"] = metric
            if override_value is None and not opts.urn:
                raise TypeError("Missing required property 'override_value'")
            __props__.__dict__["override_value"] = override_value
            __props__.__dict__["project"] = project
            if service is None and not opts.urn:
                raise TypeError("Missing required property 'service'")
            __props__.__dict__["service"] = service
            __props__.__dict__["name"] = None
        super(ConsumerQuotaOverride, __self__).__init__(
            'gcp:serviceusage/consumerQuotaOverride:ConsumerQuotaOverride',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dimensions: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            force: Optional[pulumi.Input[bool]] = None,
            limit: Optional[pulumi.Input[str]] = None,
            metric: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            override_value: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            service: Optional[pulumi.Input[str]] = None) -> 'ConsumerQuotaOverride':
        """
        Get an existing ConsumerQuotaOverride resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] dimensions: If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
        :param pulumi.Input[bool] force: If the new quota would decrease the existing quota by more than 10%, the request is rejected.
               If `force` is `true`, that safety check is ignored.
        :param pulumi.Input[str] limit: The limit on the metric, e.g. `/project/region`.
        :param pulumi.Input[str] metric: The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
        :param pulumi.Input[str] name: The server-generated name of the quota override.
        :param pulumi.Input[str] override_value: The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] service: The service that the metrics belong to, e.g. `compute.googleapis.com`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConsumerQuotaOverrideState.__new__(_ConsumerQuotaOverrideState)

        __props__.__dict__["dimensions"] = dimensions
        __props__.__dict__["force"] = force
        __props__.__dict__["limit"] = limit
        __props__.__dict__["metric"] = metric
        __props__.__dict__["name"] = name
        __props__.__dict__["override_value"] = override_value
        __props__.__dict__["project"] = project
        __props__.__dict__["service"] = service
        return ConsumerQuotaOverride(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter
    def force(self) -> pulumi.Output[Optional[bool]]:
        """
        If the new quota would decrease the existing quota by more than 10%, the request is rejected.
        If `force` is `true`, that safety check is ignored.
        """
        return pulumi.get(self, "force")

    @property
    @pulumi.getter
    def limit(self) -> pulumi.Output[str]:
        """
        The limit on the metric, e.g. `/project/region`.
        """
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter
    def metric(self) -> pulumi.Output[str]:
        """
        The metric that should be limited, e.g. `compute.googleapis.com/cpus`.
        """
        return pulumi.get(self, "metric")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The server-generated name of the quota override.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overrideValue")
    def override_value(self) -> pulumi.Output[str]:
        """
        The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
        """
        return pulumi.get(self, "override_value")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[str]:
        """
        The service that the metrics belong to, e.g. `compute.googleapis.com`.
        """
        return pulumi.get(self, "service")

