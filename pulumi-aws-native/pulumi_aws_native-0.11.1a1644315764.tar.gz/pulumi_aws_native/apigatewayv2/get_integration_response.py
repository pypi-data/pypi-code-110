# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetIntegrationResponseResult',
    'AwaitableGetIntegrationResponseResult',
    'get_integration_response',
    'get_integration_response_output',
]

@pulumi.output_type
class GetIntegrationResponseResult:
    def __init__(__self__, api_id=None, content_handling_strategy=None, id=None, integration_id=None, integration_response_key=None, response_parameters=None, response_templates=None, template_selection_expression=None):
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if content_handling_strategy and not isinstance(content_handling_strategy, str):
            raise TypeError("Expected argument 'content_handling_strategy' to be a str")
        pulumi.set(__self__, "content_handling_strategy", content_handling_strategy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if integration_id and not isinstance(integration_id, str):
            raise TypeError("Expected argument 'integration_id' to be a str")
        pulumi.set(__self__, "integration_id", integration_id)
        if integration_response_key and not isinstance(integration_response_key, str):
            raise TypeError("Expected argument 'integration_response_key' to be a str")
        pulumi.set(__self__, "integration_response_key", integration_response_key)
        if response_parameters and not isinstance(response_parameters, dict):
            raise TypeError("Expected argument 'response_parameters' to be a dict")
        pulumi.set(__self__, "response_parameters", response_parameters)
        if response_templates and not isinstance(response_templates, dict):
            raise TypeError("Expected argument 'response_templates' to be a dict")
        pulumi.set(__self__, "response_templates", response_templates)
        if template_selection_expression and not isinstance(template_selection_expression, str):
            raise TypeError("Expected argument 'template_selection_expression' to be a str")
        pulumi.set(__self__, "template_selection_expression", template_selection_expression)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[str]:
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="contentHandlingStrategy")
    def content_handling_strategy(self) -> Optional[str]:
        return pulumi.get(self, "content_handling_strategy")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="integrationId")
    def integration_id(self) -> Optional[str]:
        return pulumi.get(self, "integration_id")

    @property
    @pulumi.getter(name="integrationResponseKey")
    def integration_response_key(self) -> Optional[str]:
        return pulumi.get(self, "integration_response_key")

    @property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[Any]:
        return pulumi.get(self, "response_parameters")

    @property
    @pulumi.getter(name="responseTemplates")
    def response_templates(self) -> Optional[Any]:
        return pulumi.get(self, "response_templates")

    @property
    @pulumi.getter(name="templateSelectionExpression")
    def template_selection_expression(self) -> Optional[str]:
        return pulumi.get(self, "template_selection_expression")


class AwaitableGetIntegrationResponseResult(GetIntegrationResponseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationResponseResult(
            api_id=self.api_id,
            content_handling_strategy=self.content_handling_strategy,
            id=self.id,
            integration_id=self.integration_id,
            integration_response_key=self.integration_response_key,
            response_parameters=self.response_parameters,
            response_templates=self.response_templates,
            template_selection_expression=self.template_selection_expression)


def get_integration_response(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationResponseResult:
    """
    Resource Type definition for AWS::ApiGatewayV2::IntegrationResponse
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:apigatewayv2:getIntegrationResponse', __args__, opts=opts, typ=GetIntegrationResponseResult).value

    return AwaitableGetIntegrationResponseResult(
        api_id=__ret__.api_id,
        content_handling_strategy=__ret__.content_handling_strategy,
        id=__ret__.id,
        integration_id=__ret__.integration_id,
        integration_response_key=__ret__.integration_response_key,
        response_parameters=__ret__.response_parameters,
        response_templates=__ret__.response_templates,
        template_selection_expression=__ret__.template_selection_expression)


@_utilities.lift_output_func(get_integration_response)
def get_integration_response_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationResponseResult]:
    """
    Resource Type definition for AWS::ApiGatewayV2::IntegrationResponse
    """
    ...
