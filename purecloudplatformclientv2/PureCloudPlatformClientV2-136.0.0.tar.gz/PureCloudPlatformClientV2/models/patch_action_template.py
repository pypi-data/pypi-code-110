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

class PatchActionTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PatchActionTemplate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'media_type': 'str',
            'state': 'str',
            'content_offer': 'PatchContentOffer'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'media_type': 'mediaType',
            'state': 'state',
            'content_offer': 'contentOffer'
        }

        self._name = None
        self._description = None
        self._media_type = None
        self._state = None
        self._content_offer = None

    @property
    def name(self):
        """
        Gets the name of this PatchActionTemplate.
        Name of the action template.

        :return: The name of this PatchActionTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PatchActionTemplate.
        Name of the action template.

        :param name: The name of this PatchActionTemplate.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PatchActionTemplate.
        Description of the action template's functionality.

        :return: The description of this PatchActionTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PatchActionTemplate.
        Description of the action template's functionality.

        :param description: The description of this PatchActionTemplate.
        :type: str
        """
        
        self._description = description

    @property
    def media_type(self):
        """
        Gets the media_type of this PatchActionTemplate.
        Media type of action described by the action template.

        :return: The media_type of this PatchActionTemplate.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this PatchActionTemplate.
        Media type of action described by the action template.

        :param media_type: The media_type of this PatchActionTemplate.
        :type: str
        """
        allowed_values = ["webchat", "webMessagingOffer", "contentOffer", "integrationAction", "architectFlow", "openAction"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def state(self):
        """
        Gets the state of this PatchActionTemplate.
        Whether the action template is currently active, inactive or deleted.

        :return: The state of this PatchActionTemplate.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PatchActionTemplate.
        Whether the action template is currently active, inactive or deleted.

        :param state: The state of this PatchActionTemplate.
        :type: str
        """
        allowed_values = ["Active", "Inactive", "Deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def content_offer(self):
        """
        Gets the content_offer of this PatchActionTemplate.
        Properties used to configure an action of type content offer

        :return: The content_offer of this PatchActionTemplate.
        :rtype: PatchContentOffer
        """
        return self._content_offer

    @content_offer.setter
    def content_offer(self, content_offer):
        """
        Sets the content_offer of this PatchActionTemplate.
        Properties used to configure an action of type content offer

        :param content_offer: The content_offer of this PatchActionTemplate.
        :type: PatchContentOffer
        """
        
        self._content_offer = content_offer

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

