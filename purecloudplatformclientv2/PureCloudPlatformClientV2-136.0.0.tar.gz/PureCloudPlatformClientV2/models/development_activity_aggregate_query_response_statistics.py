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

class DevelopmentActivityAggregateQueryResponseStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DevelopmentActivityAggregateQueryResponseStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'count': 'int',
            'min': 'float',
            'max': 'float',
            'sum': 'float'
        }

        self.attribute_map = {
            'count': 'count',
            'min': 'min',
            'max': 'max',
            'sum': 'sum'
        }

        self._count = None
        self._min = None
        self._max = None
        self._sum = None

    @property
    def count(self):
        """
        Gets the count of this DevelopmentActivityAggregateQueryResponseStatistics.
        The count for this metric

        :return: The count of this DevelopmentActivityAggregateQueryResponseStatistics.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this DevelopmentActivityAggregateQueryResponseStatistics.
        The count for this metric

        :param count: The count of this DevelopmentActivityAggregateQueryResponseStatistics.
        :type: int
        """
        
        self._count = count

    @property
    def min(self):
        """
        Gets the min of this DevelopmentActivityAggregateQueryResponseStatistics.
        The minimum value in this metric

        :return: The min of this DevelopmentActivityAggregateQueryResponseStatistics.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this DevelopmentActivityAggregateQueryResponseStatistics.
        The minimum value in this metric

        :param min: The min of this DevelopmentActivityAggregateQueryResponseStatistics.
        :type: float
        """
        
        self._min = min

    @property
    def max(self):
        """
        Gets the max of this DevelopmentActivityAggregateQueryResponseStatistics.
        The maximum value in this metric

        :return: The max of this DevelopmentActivityAggregateQueryResponseStatistics.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this DevelopmentActivityAggregateQueryResponseStatistics.
        The maximum value in this metric

        :param max: The max of this DevelopmentActivityAggregateQueryResponseStatistics.
        :type: float
        """
        
        self._max = max

    @property
    def sum(self):
        """
        Gets the sum of this DevelopmentActivityAggregateQueryResponseStatistics.
        The total of the values for this metric

        :return: The sum of this DevelopmentActivityAggregateQueryResponseStatistics.
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """
        Sets the sum of this DevelopmentActivityAggregateQueryResponseStatistics.
        The total of the values for this metric

        :param sum: The sum of this DevelopmentActivityAggregateQueryResponseStatistics.
        :type: float
        """
        
        self._sum = sum

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

