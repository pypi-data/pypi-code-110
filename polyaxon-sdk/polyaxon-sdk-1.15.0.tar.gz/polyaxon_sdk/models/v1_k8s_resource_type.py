#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.15.0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from polyaxon_sdk.configuration import Configuration


class V1K8sResourceType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'schema': 'V1K8sResourceSchema',
        'is_requested': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'schema': 'schema',
        'is_requested': 'isRequested'
    }

    def __init__(self, name=None, schema=None, is_requested=None, local_vars_configuration=None):  # noqa: E501
        """V1K8sResourceType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._schema = None
        self._is_requested = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if schema is not None:
            self.schema = schema
        if is_requested is not None:
            self.is_requested = is_requested

    @property
    def name(self):
        """Gets the name of this V1K8sResourceType.  # noqa: E501


        :return: The name of this V1K8sResourceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1K8sResourceType.


        :param name: The name of this V1K8sResourceType.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def schema(self):
        """Gets the schema of this V1K8sResourceType.  # noqa: E501


        :return: The schema of this V1K8sResourceType.  # noqa: E501
        :rtype: V1K8sResourceSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this V1K8sResourceType.


        :param schema: The schema of this V1K8sResourceType.  # noqa: E501
        :type schema: V1K8sResourceSchema
        """

        self._schema = schema

    @property
    def is_requested(self):
        """Gets the is_requested of this V1K8sResourceType.  # noqa: E501


        :return: The is_requested of this V1K8sResourceType.  # noqa: E501
        :rtype: bool
        """
        return self._is_requested

    @is_requested.setter
    def is_requested(self, is_requested):
        """Sets the is_requested of this V1K8sResourceType.


        :param is_requested: The is_requested of this V1K8sResourceType.  # noqa: E501
        :type is_requested: bool
        """

        self._is_requested = is_requested

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1K8sResourceType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1K8sResourceType):
            return True

        return self.to_dict() != other.to_dict()
