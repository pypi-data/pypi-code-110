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

__all__ = ['ListenerCertificateInitArgs', 'ListenerCertificate']

@pulumi.input_type
class ListenerCertificateInitArgs:
    def __init__(__self__, *,
                 certificates: pulumi.Input[Sequence[pulumi.Input['ListenerCertificateCertificateArgs']]],
                 listener_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a ListenerCertificate resource.
        """
        pulumi.set(__self__, "certificates", certificates)
        pulumi.set(__self__, "listener_arn", listener_arn)

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Input[Sequence[pulumi.Input['ListenerCertificateCertificateArgs']]]:
        return pulumi.get(self, "certificates")

    @certificates.setter
    def certificates(self, value: pulumi.Input[Sequence[pulumi.Input['ListenerCertificateCertificateArgs']]]):
        pulumi.set(self, "certificates", value)

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "listener_arn")

    @listener_arn.setter
    def listener_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_arn", value)


warnings.warn("""ListenerCertificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ListenerCertificate(pulumi.CustomResource):
    warnings.warn("""ListenerCertificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerCertificateCertificateArgs']]]]] = None,
                 listener_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerCertificate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ListenerCertificateInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerCertificate

        :param str resource_name: The name of the resource.
        :param ListenerCertificateInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ListenerCertificateInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerCertificateCertificateArgs']]]]] = None,
                 listener_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ListenerCertificate is deprecated: ListenerCertificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ListenerCertificateInitArgs.__new__(ListenerCertificateInitArgs)

            if certificates is None and not opts.urn:
                raise TypeError("Missing required property 'certificates'")
            __props__.__dict__["certificates"] = certificates
            if listener_arn is None and not opts.urn:
                raise TypeError("Missing required property 'listener_arn'")
            __props__.__dict__["listener_arn"] = listener_arn
        super(ListenerCertificate, __self__).__init__(
            'aws-native:elasticloadbalancingv2:ListenerCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ListenerCertificate':
        """
        Get an existing ListenerCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ListenerCertificateInitArgs.__new__(ListenerCertificateInitArgs)

        __props__.__dict__["certificates"] = None
        __props__.__dict__["listener_arn"] = None
        return ListenerCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificates(self) -> pulumi.Output[Sequence['outputs.ListenerCertificateCertificate']]:
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "listener_arn")

