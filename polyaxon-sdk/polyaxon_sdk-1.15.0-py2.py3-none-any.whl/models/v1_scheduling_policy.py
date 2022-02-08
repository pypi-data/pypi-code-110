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


class V1SchedulingPolicy(object):
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
        'min_available': 'int',
        'queue': 'str',
        'priority_class': 'str'
    }

    attribute_map = {
        'min_available': 'minAvailable',
        'queue': 'queue',
        'priority_class': 'priorityClass'
    }

    def __init__(self, min_available=None, queue=None, priority_class=None, local_vars_configuration=None):  # noqa: E501
        """V1SchedulingPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._min_available = None
        self._queue = None
        self._priority_class = None
        self.discriminator = None

        if min_available is not None:
            self.min_available = min_available
        if queue is not None:
            self.queue = queue
        if priority_class is not None:
            self.priority_class = priority_class

    @property
    def min_available(self):
        """Gets the min_available of this V1SchedulingPolicy.  # noqa: E501


        :return: The min_available of this V1SchedulingPolicy.  # noqa: E501
        :rtype: int
        """
        return self._min_available

    @min_available.setter
    def min_available(self, min_available):
        """Sets the min_available of this V1SchedulingPolicy.


        :param min_available: The min_available of this V1SchedulingPolicy.  # noqa: E501
        :type min_available: int
        """

        self._min_available = min_available

    @property
    def queue(self):
        """Gets the queue of this V1SchedulingPolicy.  # noqa: E501


        :return: The queue of this V1SchedulingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this V1SchedulingPolicy.


        :param queue: The queue of this V1SchedulingPolicy.  # noqa: E501
        :type queue: str
        """

        self._queue = queue

    @property
    def priority_class(self):
        """Gets the priority_class of this V1SchedulingPolicy.  # noqa: E501


        :return: The priority_class of this V1SchedulingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._priority_class

    @priority_class.setter
    def priority_class(self, priority_class):
        """Sets the priority_class of this V1SchedulingPolicy.


        :param priority_class: The priority_class of this V1SchedulingPolicy.  # noqa: E501
        :type priority_class: str
        """

        self._priority_class = priority_class

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
        if not isinstance(other, V1SchedulingPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SchedulingPolicy):
            return True

        return self.to_dict() != other.to_dict()
