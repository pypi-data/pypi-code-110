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

class AnalyticsSessionMetric(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AnalyticsSessionMetric - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'emit_date': 'datetime',
            'name': 'str',
            'value': 'int'
        }

        self.attribute_map = {
            'emit_date': 'emitDate',
            'name': 'name',
            'value': 'value'
        }

        self._emit_date = None
        self._name = None
        self._value = None

    @property
    def emit_date(self):
        """
        Gets the emit_date of this AnalyticsSessionMetric.
        Metric emission date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The emit_date of this AnalyticsSessionMetric.
        :rtype: datetime
        """
        return self._emit_date

    @emit_date.setter
    def emit_date(self, emit_date):
        """
        Sets the emit_date of this AnalyticsSessionMetric.
        Metric emission date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param emit_date: The emit_date of this AnalyticsSessionMetric.
        :type: datetime
        """
        
        self._emit_date = emit_date

    @property
    def name(self):
        """
        Gets the name of this AnalyticsSessionMetric.
        Unique name of this metric

        :return: The name of this AnalyticsSessionMetric.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AnalyticsSessionMetric.
        Unique name of this metric

        :param name: The name of this AnalyticsSessionMetric.
        :type: str
        """
        
        self._name = name

    @property
    def value(self):
        """
        Gets the value of this AnalyticsSessionMetric.
        The metric value

        :return: The value of this AnalyticsSessionMetric.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AnalyticsSessionMetric.
        The metric value

        :param value: The value of this AnalyticsSessionMetric.
        :type: int
        """
        
        self._value = value

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

