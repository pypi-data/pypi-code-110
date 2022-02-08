# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class PhoneChangeTopicProvisionInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PhoneChangeTopicProvisionInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'time': 'datetime',
            'source': 'str',
            'error_info': 'str'
        }

        self.attribute_map = {
            'time': 'time',
            'source': 'source',
            'error_info': 'errorInfo'
        }

        self._time = None
        self._source = None
        self._error_info = None

    @property
    def time(self):
        """
        Gets the time of this PhoneChangeTopicProvisionInfo.


        :return: The time of this PhoneChangeTopicProvisionInfo.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this PhoneChangeTopicProvisionInfo.


        :param time: The time of this PhoneChangeTopicProvisionInfo.
        :type: datetime
        """
        
        self._time = time

    @property
    def source(self):
        """
        Gets the source of this PhoneChangeTopicProvisionInfo.


        :return: The source of this PhoneChangeTopicProvisionInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this PhoneChangeTopicProvisionInfo.


        :param source: The source of this PhoneChangeTopicProvisionInfo.
        :type: str
        """
        
        self._source = source

    @property
    def error_info(self):
        """
        Gets the error_info of this PhoneChangeTopicProvisionInfo.


        :return: The error_info of this PhoneChangeTopicProvisionInfo.
        :rtype: str
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """
        Sets the error_info of this PhoneChangeTopicProvisionInfo.


        :param error_info: The error_info of this PhoneChangeTopicProvisionInfo.
        :type: str
        """
        
        self._error_info = error_info

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

