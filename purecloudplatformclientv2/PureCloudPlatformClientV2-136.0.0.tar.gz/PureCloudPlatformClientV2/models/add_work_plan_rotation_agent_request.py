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

class AddWorkPlanRotationAgentRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AddWorkPlanRotationAgentRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_id': 'str',
            'date_range': 'DateRangeWithOptionalEnd',
            'position': 'int'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'date_range': 'dateRange',
            'position': 'position'
        }

        self._user_id = None
        self._date_range = None
        self._position = None

    @property
    def user_id(self):
        """
        Gets the user_id of this AddWorkPlanRotationAgentRequest.
        The ID of an agent in this work plan rotation

        :return: The user_id of this AddWorkPlanRotationAgentRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AddWorkPlanRotationAgentRequest.
        The ID of an agent in this work plan rotation

        :param user_id: The user_id of this AddWorkPlanRotationAgentRequest.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def date_range(self):
        """
        Gets the date_range of this AddWorkPlanRotationAgentRequest.
        The date range to which this agent is effective in the work plan rotation

        :return: The date_range of this AddWorkPlanRotationAgentRequest.
        :rtype: DateRangeWithOptionalEnd
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """
        Sets the date_range of this AddWorkPlanRotationAgentRequest.
        The date range to which this agent is effective in the work plan rotation

        :param date_range: The date_range of this AddWorkPlanRotationAgentRequest.
        :type: DateRangeWithOptionalEnd
        """
        
        self._date_range = date_range

    @property
    def position(self):
        """
        Gets the position of this AddWorkPlanRotationAgentRequest.
        Start position of the work plan in the pattern for this agent in the work plan rotation. Position value starts from 0

        :return: The position of this AddWorkPlanRotationAgentRequest.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this AddWorkPlanRotationAgentRequest.
        Start position of the work plan in the pattern for this agent in the work plan rotation. Position value starts from 0

        :param position: The position of this AddWorkPlanRotationAgentRequest.
        :type: int
        """
        
        self._position = position

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

