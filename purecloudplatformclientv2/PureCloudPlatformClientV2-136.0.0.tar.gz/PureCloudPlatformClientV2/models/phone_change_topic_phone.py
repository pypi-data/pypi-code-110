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

class PhoneChangeTopicPhone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PhoneChangeTopicPhone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_agent_info': 'PhoneChangeTopicUserAgentInfo',
            'id': 'str',
            'status': 'PhoneChangeTopicPhoneStatus',
            'secondary_status': 'PhoneChangeTopicPhoneStatus'
        }

        self.attribute_map = {
            'user_agent_info': 'userAgentInfo',
            'id': 'id',
            'status': 'status',
            'secondary_status': 'secondaryStatus'
        }

        self._user_agent_info = None
        self._id = None
        self._status = None
        self._secondary_status = None

    @property
    def user_agent_info(self):
        """
        Gets the user_agent_info of this PhoneChangeTopicPhone.


        :return: The user_agent_info of this PhoneChangeTopicPhone.
        :rtype: PhoneChangeTopicUserAgentInfo
        """
        return self._user_agent_info

    @user_agent_info.setter
    def user_agent_info(self, user_agent_info):
        """
        Sets the user_agent_info of this PhoneChangeTopicPhone.


        :param user_agent_info: The user_agent_info of this PhoneChangeTopicPhone.
        :type: PhoneChangeTopicUserAgentInfo
        """
        
        self._user_agent_info = user_agent_info

    @property
    def id(self):
        """
        Gets the id of this PhoneChangeTopicPhone.


        :return: The id of this PhoneChangeTopicPhone.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PhoneChangeTopicPhone.


        :param id: The id of this PhoneChangeTopicPhone.
        :type: str
        """
        
        self._id = id

    @property
    def status(self):
        """
        Gets the status of this PhoneChangeTopicPhone.


        :return: The status of this PhoneChangeTopicPhone.
        :rtype: PhoneChangeTopicPhoneStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PhoneChangeTopicPhone.


        :param status: The status of this PhoneChangeTopicPhone.
        :type: PhoneChangeTopicPhoneStatus
        """
        
        self._status = status

    @property
    def secondary_status(self):
        """
        Gets the secondary_status of this PhoneChangeTopicPhone.


        :return: The secondary_status of this PhoneChangeTopicPhone.
        :rtype: PhoneChangeTopicPhoneStatus
        """
        return self._secondary_status

    @secondary_status.setter
    def secondary_status(self, secondary_status):
        """
        Sets the secondary_status of this PhoneChangeTopicPhone.


        :param secondary_status: The secondary_status of this PhoneChangeTopicPhone.
        :type: PhoneChangeTopicPhoneStatus
        """
        
        self._secondary_status = secondary_status

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

