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

class ConversationEventTopicDialerPreview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationEventTopicDialerPreview - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'contact_id': 'str',
            'contact_list_id': 'str',
            'campaign_id': 'str',
            'phone_number_columns': 'list[ConversationEventTopicPhoneNumberColumn]'
        }

        self.attribute_map = {
            'id': 'id',
            'contact_id': 'contactId',
            'contact_list_id': 'contactListId',
            'campaign_id': 'campaignId',
            'phone_number_columns': 'phoneNumberColumns'
        }

        self._id = None
        self._contact_id = None
        self._contact_list_id = None
        self._campaign_id = None
        self._phone_number_columns = None

    @property
    def id(self):
        """
        Gets the id of this ConversationEventTopicDialerPreview.


        :return: The id of this ConversationEventTopicDialerPreview.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConversationEventTopicDialerPreview.


        :param id: The id of this ConversationEventTopicDialerPreview.
        :type: str
        """
        
        self._id = id

    @property
    def contact_id(self):
        """
        Gets the contact_id of this ConversationEventTopicDialerPreview.
        The contact associated with this preview data pop

        :return: The contact_id of this ConversationEventTopicDialerPreview.
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """
        Sets the contact_id of this ConversationEventTopicDialerPreview.
        The contact associated with this preview data pop

        :param contact_id: The contact_id of this ConversationEventTopicDialerPreview.
        :type: str
        """
        
        self._contact_id = contact_id

    @property
    def contact_list_id(self):
        """
        Gets the contact_list_id of this ConversationEventTopicDialerPreview.
        The contactList associated with this preview data pop.

        :return: The contact_list_id of this ConversationEventTopicDialerPreview.
        :rtype: str
        """
        return self._contact_list_id

    @contact_list_id.setter
    def contact_list_id(self, contact_list_id):
        """
        Sets the contact_list_id of this ConversationEventTopicDialerPreview.
        The contactList associated with this preview data pop.

        :param contact_list_id: The contact_list_id of this ConversationEventTopicDialerPreview.
        :type: str
        """
        
        self._contact_list_id = contact_list_id

    @property
    def campaign_id(self):
        """
        Gets the campaign_id of this ConversationEventTopicDialerPreview.
        The campaignId associated with this preview data pop.

        :return: The campaign_id of this ConversationEventTopicDialerPreview.
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """
        Sets the campaign_id of this ConversationEventTopicDialerPreview.
        The campaignId associated with this preview data pop.

        :param campaign_id: The campaign_id of this ConversationEventTopicDialerPreview.
        :type: str
        """
        
        self._campaign_id = campaign_id

    @property
    def phone_number_columns(self):
        """
        Gets the phone_number_columns of this ConversationEventTopicDialerPreview.
        The phone number columns associated with this campaign

        :return: The phone_number_columns of this ConversationEventTopicDialerPreview.
        :rtype: list[ConversationEventTopicPhoneNumberColumn]
        """
        return self._phone_number_columns

    @phone_number_columns.setter
    def phone_number_columns(self, phone_number_columns):
        """
        Sets the phone_number_columns of this ConversationEventTopicDialerPreview.
        The phone number columns associated with this campaign

        :param phone_number_columns: The phone_number_columns of this ConversationEventTopicDialerPreview.
        :type: list[ConversationEventTopicPhoneNumberColumn]
        """
        
        self._phone_number_columns = phone_number_columns

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

