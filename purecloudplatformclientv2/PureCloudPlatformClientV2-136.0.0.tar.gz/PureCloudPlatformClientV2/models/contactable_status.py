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

class ContactableStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContactableStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contactable': 'bool',
            'column_status': 'dict(str, ColumnStatus)'
        }

        self.attribute_map = {
            'contactable': 'contactable',
            'column_status': 'columnStatus'
        }

        self._contactable = None
        self._column_status = None

    @property
    def contactable(self):
        """
        Gets the contactable of this ContactableStatus.
        Indicates whether or not the entire contact is contactable for the associated media type.

        :return: The contactable of this ContactableStatus.
        :rtype: bool
        """
        return self._contactable

    @contactable.setter
    def contactable(self, contactable):
        """
        Sets the contactable of this ContactableStatus.
        Indicates whether or not the entire contact is contactable for the associated media type.

        :param contactable: The contactable of this ContactableStatus.
        :type: bool
        """
        
        self._contactable = contactable

    @property
    def column_status(self):
        """
        Gets the column_status of this ContactableStatus.
        A map of individual contact method columns to whether the individual column is contactable for the associated media type.

        :return: The column_status of this ContactableStatus.
        :rtype: dict(str, ColumnStatus)
        """
        return self._column_status

    @column_status.setter
    def column_status(self, column_status):
        """
        Sets the column_status of this ContactableStatus.
        A map of individual contact method columns to whether the individual column is contactable for the associated media type.

        :param column_status: The column_status of this ContactableStatus.
        :type: dict(str, ColumnStatus)
        """
        
        self._column_status = column_status

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

