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

class AttendanceStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AttendanceStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date_workday': 'date',
            'attendance_status_type': 'str'
        }

        self.attribute_map = {
            'date_workday': 'dateWorkday',
            'attendance_status_type': 'attendanceStatusType'
        }

        self._date_workday = None
        self._attendance_status_type = None

    @property
    def date_workday(self):
        """
        Gets the date_workday of this AttendanceStatus.
        the workday date of this attendance status. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The date_workday of this AttendanceStatus.
        :rtype: date
        """
        return self._date_workday

    @date_workday.setter
    def date_workday(self, date_workday):
        """
        Sets the date_workday of this AttendanceStatus.
        the workday date of this attendance status. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param date_workday: The date_workday of this AttendanceStatus.
        :type: date
        """
        
        self._date_workday = date_workday

    @property
    def attendance_status_type(self):
        """
        Gets the attendance_status_type of this AttendanceStatus.
        the attendance status

        :return: The attendance_status_type of this AttendanceStatus.
        :rtype: str
        """
        return self._attendance_status_type

    @attendance_status_type.setter
    def attendance_status_type(self, attendance_status_type):
        """
        Sets the attendance_status_type of this AttendanceStatus.
        the attendance status

        :param attendance_status_type: The attendance_status_type of this AttendanceStatus.
        :type: str
        """
        allowed_values = ["HasData", "Scheduled", "Absent", "Present", "NoSchedule"]
        if attendance_status_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for attendance_status_type -> " + attendance_status_type)
            self._attendance_status_type = "outdated_sdk_version"
        else:
            self._attendance_status_type = attendance_status_type

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

