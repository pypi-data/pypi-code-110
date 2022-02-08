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

class WebMessagingButtonResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WebMessagingButtonResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'text': 'str',
            'payload': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'text': 'text',
            'payload': 'payload'
        }

        self._id = None
        self._type = None
        self._text = None
        self._payload = None

    @property
    def id(self):
        """
        Gets the id of this WebMessagingButtonResponse.
        An ID assigned to the button response (Deprecated).

        :return: The id of this WebMessagingButtonResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WebMessagingButtonResponse.
        An ID assigned to the button response (Deprecated).

        :param id: The id of this WebMessagingButtonResponse.
        :type: str
        """
        
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this WebMessagingButtonResponse.
        Describes the button that resulted in the Button Response.

        :return: The type of this WebMessagingButtonResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WebMessagingButtonResponse.
        Describes the button that resulted in the Button Response.

        :param type: The type of this WebMessagingButtonResponse.
        :type: str
        """
        allowed_values = ["Button", "QuickReply"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def text(self):
        """
        Gets the text of this WebMessagingButtonResponse.
        The response text from the button click.

        :return: The text of this WebMessagingButtonResponse.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this WebMessagingButtonResponse.
        The response text from the button click.

        :param text: The text of this WebMessagingButtonResponse.
        :type: str
        """
        
        self._text = text

    @property
    def payload(self):
        """
        Gets the payload of this WebMessagingButtonResponse.
        The response payload associated with the clicked button.

        :return: The payload of this WebMessagingButtonResponse.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this WebMessagingButtonResponse.
        The response payload associated with the clicked button.

        :param payload: The payload of this WebMessagingButtonResponse.
        :type: str
        """
        
        self._payload = payload

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

