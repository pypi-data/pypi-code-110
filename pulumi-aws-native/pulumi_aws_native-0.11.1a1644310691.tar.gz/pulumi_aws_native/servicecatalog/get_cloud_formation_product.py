# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetCloudFormationProductResult',
    'AwaitableGetCloudFormationProductResult',
    'get_cloud_formation_product',
    'get_cloud_formation_product_output',
]

@pulumi.output_type
class GetCloudFormationProductResult:
    def __init__(__self__, accept_language=None, description=None, distributor=None, id=None, name=None, owner=None, product_name=None, provisioning_artifact_ids=None, provisioning_artifact_names=None, provisioning_artifact_parameters=None, replace_provisioning_artifacts=None, support_description=None, support_email=None, support_url=None, tags=None):
        if accept_language and not isinstance(accept_language, str):
            raise TypeError("Expected argument 'accept_language' to be a str")
        pulumi.set(__self__, "accept_language", accept_language)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if distributor and not isinstance(distributor, str):
            raise TypeError("Expected argument 'distributor' to be a str")
        pulumi.set(__self__, "distributor", distributor)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if product_name and not isinstance(product_name, str):
            raise TypeError("Expected argument 'product_name' to be a str")
        pulumi.set(__self__, "product_name", product_name)
        if provisioning_artifact_ids and not isinstance(provisioning_artifact_ids, str):
            raise TypeError("Expected argument 'provisioning_artifact_ids' to be a str")
        pulumi.set(__self__, "provisioning_artifact_ids", provisioning_artifact_ids)
        if provisioning_artifact_names and not isinstance(provisioning_artifact_names, str):
            raise TypeError("Expected argument 'provisioning_artifact_names' to be a str")
        pulumi.set(__self__, "provisioning_artifact_names", provisioning_artifact_names)
        if provisioning_artifact_parameters and not isinstance(provisioning_artifact_parameters, list):
            raise TypeError("Expected argument 'provisioning_artifact_parameters' to be a list")
        pulumi.set(__self__, "provisioning_artifact_parameters", provisioning_artifact_parameters)
        if replace_provisioning_artifacts and not isinstance(replace_provisioning_artifacts, bool):
            raise TypeError("Expected argument 'replace_provisioning_artifacts' to be a bool")
        pulumi.set(__self__, "replace_provisioning_artifacts", replace_provisioning_artifacts)
        if support_description and not isinstance(support_description, str):
            raise TypeError("Expected argument 'support_description' to be a str")
        pulumi.set(__self__, "support_description", support_description)
        if support_email and not isinstance(support_email, str):
            raise TypeError("Expected argument 'support_email' to be a str")
        pulumi.set(__self__, "support_email", support_email)
        if support_url and not isinstance(support_url, str):
            raise TypeError("Expected argument 'support_url' to be a str")
        pulumi.set(__self__, "support_url", support_url)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[str]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def distributor(self) -> Optional[str]:
        return pulumi.get(self, "distributor")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> Optional[str]:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[str]:
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="provisioningArtifactIds")
    def provisioning_artifact_ids(self) -> Optional[str]:
        return pulumi.get(self, "provisioning_artifact_ids")

    @property
    @pulumi.getter(name="provisioningArtifactNames")
    def provisioning_artifact_names(self) -> Optional[str]:
        return pulumi.get(self, "provisioning_artifact_names")

    @property
    @pulumi.getter(name="provisioningArtifactParameters")
    def provisioning_artifact_parameters(self) -> Optional[Sequence['outputs.CloudFormationProductProvisioningArtifactProperties']]:
        return pulumi.get(self, "provisioning_artifact_parameters")

    @property
    @pulumi.getter(name="replaceProvisioningArtifacts")
    def replace_provisioning_artifacts(self) -> Optional[bool]:
        return pulumi.get(self, "replace_provisioning_artifacts")

    @property
    @pulumi.getter(name="supportDescription")
    def support_description(self) -> Optional[str]:
        return pulumi.get(self, "support_description")

    @property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> Optional[str]:
        return pulumi.get(self, "support_email")

    @property
    @pulumi.getter(name="supportUrl")
    def support_url(self) -> Optional[str]:
        return pulumi.get(self, "support_url")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CloudFormationProductTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetCloudFormationProductResult(GetCloudFormationProductResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudFormationProductResult(
            accept_language=self.accept_language,
            description=self.description,
            distributor=self.distributor,
            id=self.id,
            name=self.name,
            owner=self.owner,
            product_name=self.product_name,
            provisioning_artifact_ids=self.provisioning_artifact_ids,
            provisioning_artifact_names=self.provisioning_artifact_names,
            provisioning_artifact_parameters=self.provisioning_artifact_parameters,
            replace_provisioning_artifacts=self.replace_provisioning_artifacts,
            support_description=self.support_description,
            support_email=self.support_email,
            support_url=self.support_url,
            tags=self.tags)


def get_cloud_formation_product(id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudFormationProductResult:
    """
    Resource Type definition for AWS::ServiceCatalog::CloudFormationProduct
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalog:getCloudFormationProduct', __args__, opts=opts, typ=GetCloudFormationProductResult).value

    return AwaitableGetCloudFormationProductResult(
        accept_language=__ret__.accept_language,
        description=__ret__.description,
        distributor=__ret__.distributor,
        id=__ret__.id,
        name=__ret__.name,
        owner=__ret__.owner,
        product_name=__ret__.product_name,
        provisioning_artifact_ids=__ret__.provisioning_artifact_ids,
        provisioning_artifact_names=__ret__.provisioning_artifact_names,
        provisioning_artifact_parameters=__ret__.provisioning_artifact_parameters,
        replace_provisioning_artifacts=__ret__.replace_provisioning_artifacts,
        support_description=__ret__.support_description,
        support_email=__ret__.support_email,
        support_url=__ret__.support_url,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_cloud_formation_product)
def get_cloud_formation_product_output(id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudFormationProductResult]:
    """
    Resource Type definition for AWS::ServiceCatalog::CloudFormationProduct
    """
    ...
