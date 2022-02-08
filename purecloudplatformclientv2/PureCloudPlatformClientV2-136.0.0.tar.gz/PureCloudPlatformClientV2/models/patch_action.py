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

class PatchAction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PatchAction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'media_type': 'str',
            'action_template': 'ActionMapActionTemplate',
            'architect_flow_fields': 'ArchitectFlowFields',
            'web_messaging_offer_fields': 'WebMessagingOfferFields',
            'open_action_fields': 'OpenActionFields'
        }

        self.attribute_map = {
            'media_type': 'mediaType',
            'action_template': 'actionTemplate',
            'architect_flow_fields': 'architectFlowFields',
            'web_messaging_offer_fields': 'webMessagingOfferFields',
            'open_action_fields': 'openActionFields'
        }

        self._media_type = None
        self._action_template = None
        self._architect_flow_fields = None
        self._web_messaging_offer_fields = None
        self._open_action_fields = None

    @property
    def media_type(self):
        """
        Gets the media_type of this PatchAction.
        Media type of action.

        :return: The media_type of this PatchAction.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this PatchAction.
        Media type of action.

        :param media_type: The media_type of this PatchAction.
        :type: str
        """
        allowed_values = ["webchat", "webMessagingOffer", "contentOffer", "integrationAction", "architectFlow", "openAction"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def action_template(self):
        """
        Gets the action_template of this PatchAction.
        Action template associated with the action map.

        :return: The action_template of this PatchAction.
        :rtype: ActionMapActionTemplate
        """
        return self._action_template

    @action_template.setter
    def action_template(self, action_template):
        """
        Sets the action_template of this PatchAction.
        Action template associated with the action map.

        :param action_template: The action_template of this PatchAction.
        :type: ActionMapActionTemplate
        """
        
        self._action_template = action_template

    @property
    def architect_flow_fields(self):
        """
        Gets the architect_flow_fields of this PatchAction.
        Architect Flow Id and input contract.

        :return: The architect_flow_fields of this PatchAction.
        :rtype: ArchitectFlowFields
        """
        return self._architect_flow_fields

    @architect_flow_fields.setter
    def architect_flow_fields(self, architect_flow_fields):
        """
        Sets the architect_flow_fields of this PatchAction.
        Architect Flow Id and input contract.

        :param architect_flow_fields: The architect_flow_fields of this PatchAction.
        :type: ArchitectFlowFields
        """
        
        self._architect_flow_fields = architect_flow_fields

    @property
    def web_messaging_offer_fields(self):
        """
        Gets the web_messaging_offer_fields of this PatchAction.
        Admin-configurable fields of a web messaging offer action.

        :return: The web_messaging_offer_fields of this PatchAction.
        :rtype: WebMessagingOfferFields
        """
        return self._web_messaging_offer_fields

    @web_messaging_offer_fields.setter
    def web_messaging_offer_fields(self, web_messaging_offer_fields):
        """
        Sets the web_messaging_offer_fields of this PatchAction.
        Admin-configurable fields of a web messaging offer action.

        :param web_messaging_offer_fields: The web_messaging_offer_fields of this PatchAction.
        :type: WebMessagingOfferFields
        """
        
        self._web_messaging_offer_fields = web_messaging_offer_fields

    @property
    def open_action_fields(self):
        """
        Gets the open_action_fields of this PatchAction.
        Admin-configurable fields of an open action.

        :return: The open_action_fields of this PatchAction.
        :rtype: OpenActionFields
        """
        return self._open_action_fields

    @open_action_fields.setter
    def open_action_fields(self, open_action_fields):
        """
        Sets the open_action_fields of this PatchAction.
        Admin-configurable fields of an open action.

        :param open_action_fields: The open_action_fields of this PatchAction.
        :type: OpenActionFields
        """
        
        self._open_action_fields = open_action_fields

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

