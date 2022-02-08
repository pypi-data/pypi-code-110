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

class UserAgentInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserAgentInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'firmware_version': 'str',
            'manufacturer': 'str',
            'model': 'str'
        }

        self.attribute_map = {
            'firmware_version': 'firmwareVersion',
            'manufacturer': 'manufacturer',
            'model': 'model'
        }

        self._firmware_version = None
        self._manufacturer = None
        self._model = None

    @property
    def firmware_version(self):
        """
        Gets the firmware_version of this UserAgentInfo.
        The firmware version of the phone.

        :return: The firmware_version of this UserAgentInfo.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """
        Sets the firmware_version of this UserAgentInfo.
        The firmware version of the phone.

        :param firmware_version: The firmware_version of this UserAgentInfo.
        :type: str
        """
        
        self._firmware_version = firmware_version

    @property
    def manufacturer(self):
        """
        Gets the manufacturer of this UserAgentInfo.
        The manufacturer of the phone.

        :return: The manufacturer of this UserAgentInfo.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """
        Sets the manufacturer of this UserAgentInfo.
        The manufacturer of the phone.

        :param manufacturer: The manufacturer of this UserAgentInfo.
        :type: str
        """
        
        self._manufacturer = manufacturer

    @property
    def model(self):
        """
        Gets the model of this UserAgentInfo.
        The model of the phone.

        :return: The model of this UserAgentInfo.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this UserAgentInfo.
        The model of the phone.

        :param model: The model of this UserAgentInfo.
        :type: str
        """
        
        self._model = model

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

