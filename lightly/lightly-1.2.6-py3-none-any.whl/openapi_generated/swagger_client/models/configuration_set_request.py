# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class ConfigurationSetRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'configs': 'list[ConfigurationEntry]'
    }

    attribute_map = {
        'name': 'name',
        'configs': 'configs'
    }

    def __init__(self, name=None, configs=None, _configuration=None):  # noqa: E501
        """ConfigurationSetRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._configs = None
        self.discriminator = None

        self.name = name
        self.configs = configs

    @property
    def name(self):
        """Gets the name of this ConfigurationSetRequest.  # noqa: E501


        :return: The name of this ConfigurationSetRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationSetRequest.


        :param name: The name of this ConfigurationSetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def configs(self):
        """Gets the configs of this ConfigurationSetRequest.  # noqa: E501


        :return: The configs of this ConfigurationSetRequest.  # noqa: E501
        :rtype: list[ConfigurationEntry]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ConfigurationSetRequest.


        :param configs: The configs of this ConfigurationSetRequest.  # noqa: E501
        :type: list[ConfigurationEntry]
        """
        if self._configuration.client_side_validation and configs is None:
            raise ValueError("Invalid value for `configs`, must not be `None`")  # noqa: E501

        self._configs = configs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConfigurationSetRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigurationSetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigurationSetRequest):
            return True

        return self.to_dict() != other.to_dict()
