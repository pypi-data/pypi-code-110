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

class Recipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Recipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'flow': 'Flow',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'created_by': 'User',
            'modified_by': 'User',
            'messenger_type': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'flow': 'flow',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'created_by': 'createdBy',
            'modified_by': 'modifiedBy',
            'messenger_type': 'messengerType',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._flow = None
        self._date_created = None
        self._date_modified = None
        self._created_by = None
        self._modified_by = None
        self._messenger_type = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Recipient.
        The globally unique identifier for the object.

        :return: The id of this Recipient.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Recipient.
        The globally unique identifier for the object.

        :param id: The id of this Recipient.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Recipient.


        :return: The name of this Recipient.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Recipient.


        :param name: The name of this Recipient.
        :type: str
        """
        
        self._name = name

    @property
    def flow(self):
        """
        Gets the flow of this Recipient.
        An automate flow object which defines the set of actions to be taken, when a message is received by this provisioned phone number.

        :return: The flow of this Recipient.
        :rtype: Flow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """
        Sets the flow of this Recipient.
        An automate flow object which defines the set of actions to be taken, when a message is received by this provisioned phone number.

        :param flow: The flow of this Recipient.
        :type: Flow
        """
        
        self._flow = flow

    @property
    def date_created(self):
        """
        Gets the date_created of this Recipient.
        Date this recipient was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Recipient.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Recipient.
        Date this recipient was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Recipient.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def date_modified(self):
        """
        Gets the date_modified of this Recipient.
        Date this recipient was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Recipient.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this Recipient.
        Date this recipient was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Recipient.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def created_by(self):
        """
        Gets the created_by of this Recipient.
        User that created this recipient

        :return: The created_by of this Recipient.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Recipient.
        User that created this recipient

        :param created_by: The created_by of this Recipient.
        :type: User
        """
        
        self._created_by = created_by

    @property
    def modified_by(self):
        """
        Gets the modified_by of this Recipient.
        User that modified this recipient

        :return: The modified_by of this Recipient.
        :rtype: User
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this Recipient.
        User that modified this recipient

        :param modified_by: The modified_by of this Recipient.
        :type: User
        """
        
        self._modified_by = modified_by

    @property
    def messenger_type(self):
        """
        Gets the messenger_type of this Recipient.
        The messenger type for this recipient

        :return: The messenger_type of this Recipient.
        :rtype: str
        """
        return self._messenger_type

    @messenger_type.setter
    def messenger_type(self, messenger_type):
        """
        Sets the messenger_type of this Recipient.
        The messenger type for this recipient

        :param messenger_type: The messenger_type of this Recipient.
        :type: str
        """
        allowed_values = ["sms", "facebook", "twitter", "line", "whatsapp", "webmessaging", "instagram", "open"]
        if messenger_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for messenger_type -> " + messenger_type)
            self._messenger_type = "outdated_sdk_version"
        else:
            self._messenger_type = messenger_type

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Recipient.
        The URI for this object

        :return: The self_uri of this Recipient.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Recipient.
        The URI for this object

        :param self_uri: The self_uri of this Recipient.
        :type: str
        """
        
        self._self_uri = self_uri

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

