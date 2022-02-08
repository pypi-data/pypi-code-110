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

__all__ = ['EventSubscriptionArgs', 'EventSubscription']

@pulumi.input_type
class EventSubscriptionArgs:
    def __init__(__self__, *,
                 sns_topic_arn: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 event_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]]] = None):
        """
        The set of arguments for constructing a EventSubscription resource.
        """
        pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if event_categories is not None:
            pulumi.set(__self__, "event_categories", event_categories)
        if source_ids is not None:
            pulumi.set(__self__, "source_ids", source_ids)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)
        if subscription_name is not None:
            pulumi.set(__self__, "subscription_name", subscription_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "sns_topic_arn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "sns_topic_arn", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="eventCategories")
    def event_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "event_categories")

    @event_categories.setter
    def event_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "event_categories", value)

    @property
    @pulumi.getter(name="sourceIds")
    def source_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "source_ids")

    @source_ids.setter
    def source_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "source_ids", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "subscription_name")

    @subscription_name.setter
    def subscription_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EventSubscriptionTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""EventSubscription is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class EventSubscription(pulumi.CustomResource):
    warnings.warn("""EventSubscription is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 event_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 source_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventSubscriptionTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::DMS::EventSubscription

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::DMS::EventSubscription

        :param str resource_name: The name of the resource.
        :param EventSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 event_categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 source_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EventSubscriptionTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""EventSubscription is deprecated: EventSubscription is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventSubscriptionArgs.__new__(EventSubscriptionArgs)

            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["event_categories"] = event_categories
            if sns_topic_arn is None and not opts.urn:
                raise TypeError("Missing required property 'sns_topic_arn'")
            __props__.__dict__["sns_topic_arn"] = sns_topic_arn
            __props__.__dict__["source_ids"] = source_ids
            __props__.__dict__["source_type"] = source_type
            __props__.__dict__["subscription_name"] = subscription_name
            __props__.__dict__["tags"] = tags
        super(EventSubscription, __self__).__init__(
            'aws-native:dms:EventSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventSubscription':
        """
        Get an existing EventSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventSubscriptionArgs.__new__(EventSubscriptionArgs)

        __props__.__dict__["enabled"] = None
        __props__.__dict__["event_categories"] = None
        __props__.__dict__["sns_topic_arn"] = None
        __props__.__dict__["source_ids"] = None
        __props__.__dict__["source_type"] = None
        __props__.__dict__["subscription_name"] = None
        __props__.__dict__["tags"] = None
        return EventSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="eventCategories")
    def event_categories(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "event_categories")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "sns_topic_arn")

    @property
    @pulumi.getter(name="sourceIds")
    def source_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "source_ids")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "subscription_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.EventSubscriptionTag']]]:
        return pulumi.get(self, "tags")

