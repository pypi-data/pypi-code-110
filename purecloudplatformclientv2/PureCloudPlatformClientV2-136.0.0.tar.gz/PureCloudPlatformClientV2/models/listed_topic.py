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

class ListedTopic(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ListedTopic - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'published': 'bool',
            'strictness': 'str',
            'programs_count': 'int',
            'tags': 'list[str]',
            'dialect': 'str',
            'participants': 'str',
            'phrases_count': 'int',
            'modified_by': 'AddressableEntityRef',
            'date_modified': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'published': 'published',
            'strictness': 'strictness',
            'programs_count': 'programsCount',
            'tags': 'tags',
            'dialect': 'dialect',
            'participants': 'participants',
            'phrases_count': 'phrasesCount',
            'modified_by': 'modifiedBy',
            'date_modified': 'dateModified',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._published = None
        self._strictness = None
        self._programs_count = None
        self._tags = None
        self._dialect = None
        self._participants = None
        self._phrases_count = None
        self._modified_by = None
        self._date_modified = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this ListedTopic.
        The globally unique identifier for the object.

        :return: The id of this ListedTopic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ListedTopic.
        The globally unique identifier for the object.

        :param id: The id of this ListedTopic.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ListedTopic.


        :return: The name of this ListedTopic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ListedTopic.


        :param name: The name of this ListedTopic.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ListedTopic.


        :return: The description of this ListedTopic.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ListedTopic.


        :param description: The description of this ListedTopic.
        :type: str
        """
        
        self._description = description

    @property
    def published(self):
        """
        Gets the published of this ListedTopic.


        :return: The published of this ListedTopic.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this ListedTopic.


        :param published: The published of this ListedTopic.
        :type: bool
        """
        
        self._published = published

    @property
    def strictness(self):
        """
        Gets the strictness of this ListedTopic.


        :return: The strictness of this ListedTopic.
        :rtype: str
        """
        return self._strictness

    @strictness.setter
    def strictness(self, strictness):
        """
        Sets the strictness of this ListedTopic.


        :param strictness: The strictness of this ListedTopic.
        :type: str
        """
        allowed_values = ["1", "55", "65", "72", "85", "90"]
        if strictness.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for strictness -> " + strictness)
            self._strictness = "outdated_sdk_version"
        else:
            self._strictness = strictness

    @property
    def programs_count(self):
        """
        Gets the programs_count of this ListedTopic.


        :return: The programs_count of this ListedTopic.
        :rtype: int
        """
        return self._programs_count

    @programs_count.setter
    def programs_count(self, programs_count):
        """
        Sets the programs_count of this ListedTopic.


        :param programs_count: The programs_count of this ListedTopic.
        :type: int
        """
        
        self._programs_count = programs_count

    @property
    def tags(self):
        """
        Gets the tags of this ListedTopic.


        :return: The tags of this ListedTopic.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ListedTopic.


        :param tags: The tags of this ListedTopic.
        :type: list[str]
        """
        
        self._tags = tags

    @property
    def dialect(self):
        """
        Gets the dialect of this ListedTopic.


        :return: The dialect of this ListedTopic.
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """
        Sets the dialect of this ListedTopic.


        :param dialect: The dialect of this ListedTopic.
        :type: str
        """
        
        self._dialect = dialect

    @property
    def participants(self):
        """
        Gets the participants of this ListedTopic.


        :return: The participants of this ListedTopic.
        :rtype: str
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """
        Sets the participants of this ListedTopic.


        :param participants: The participants of this ListedTopic.
        :type: str
        """
        allowed_values = ["External", "Internal", "All"]
        if participants.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for participants -> " + participants)
            self._participants = "outdated_sdk_version"
        else:
            self._participants = participants

    @property
    def phrases_count(self):
        """
        Gets the phrases_count of this ListedTopic.


        :return: The phrases_count of this ListedTopic.
        :rtype: int
        """
        return self._phrases_count

    @phrases_count.setter
    def phrases_count(self, phrases_count):
        """
        Sets the phrases_count of this ListedTopic.


        :param phrases_count: The phrases_count of this ListedTopic.
        :type: int
        """
        
        self._phrases_count = phrases_count

    @property
    def modified_by(self):
        """
        Gets the modified_by of this ListedTopic.


        :return: The modified_by of this ListedTopic.
        :rtype: AddressableEntityRef
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this ListedTopic.


        :param modified_by: The modified_by of this ListedTopic.
        :type: AddressableEntityRef
        """
        
        self._modified_by = modified_by

    @property
    def date_modified(self):
        """
        Gets the date_modified of this ListedTopic.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this ListedTopic.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this ListedTopic.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this ListedTopic.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def self_uri(self):
        """
        Gets the self_uri of this ListedTopic.
        The URI for this object

        :return: The self_uri of this ListedTopic.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this ListedTopic.
        The URI for this object

        :param self_uri: The self_uri of this ListedTopic.
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

