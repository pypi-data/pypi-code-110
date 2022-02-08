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

class CrossPlatformPolicyCreate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CrossPlatformPolicyCreate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'modified_date': 'datetime',
            'created_date': 'datetime',
            'order': 'int',
            'description': 'str',
            'enabled': 'bool',
            'media_policies': 'CrossPlatformMediaPolicies',
            'conditions': 'PolicyConditions',
            'actions': 'CrossPlatformPolicyActions',
            'policy_errors': 'PolicyErrors',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'modified_date': 'modifiedDate',
            'created_date': 'createdDate',
            'order': 'order',
            'description': 'description',
            'enabled': 'enabled',
            'media_policies': 'mediaPolicies',
            'conditions': 'conditions',
            'actions': 'actions',
            'policy_errors': 'policyErrors',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._modified_date = None
        self._created_date = None
        self._order = None
        self._description = None
        self._enabled = None
        self._media_policies = None
        self._conditions = None
        self._actions = None
        self._policy_errors = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this CrossPlatformPolicyCreate.
        The globally unique identifier for the object.

        :return: The id of this CrossPlatformPolicyCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CrossPlatformPolicyCreate.
        The globally unique identifier for the object.

        :param id: The id of this CrossPlatformPolicyCreate.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CrossPlatformPolicyCreate.
        The policy name.

        :return: The name of this CrossPlatformPolicyCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CrossPlatformPolicyCreate.
        The policy name.

        :param name: The name of this CrossPlatformPolicyCreate.
        :type: str
        """
        
        self._name = name

    @property
    def modified_date(self):
        """
        Gets the modified_date of this CrossPlatformPolicyCreate.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modified_date of this CrossPlatformPolicyCreate.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this CrossPlatformPolicyCreate.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modified_date: The modified_date of this CrossPlatformPolicyCreate.
        :type: datetime
        """
        
        self._modified_date = modified_date

    @property
    def created_date(self):
        """
        Gets the created_date of this CrossPlatformPolicyCreate.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_date of this CrossPlatformPolicyCreate.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this CrossPlatformPolicyCreate.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_date: The created_date of this CrossPlatformPolicyCreate.
        :type: datetime
        """
        
        self._created_date = created_date

    @property
    def order(self):
        """
        Gets the order of this CrossPlatformPolicyCreate.


        :return: The order of this CrossPlatformPolicyCreate.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this CrossPlatformPolicyCreate.


        :param order: The order of this CrossPlatformPolicyCreate.
        :type: int
        """
        
        self._order = order

    @property
    def description(self):
        """
        Gets the description of this CrossPlatformPolicyCreate.


        :return: The description of this CrossPlatformPolicyCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CrossPlatformPolicyCreate.


        :param description: The description of this CrossPlatformPolicyCreate.
        :type: str
        """
        
        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this CrossPlatformPolicyCreate.


        :return: The enabled of this CrossPlatformPolicyCreate.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CrossPlatformPolicyCreate.


        :param enabled: The enabled of this CrossPlatformPolicyCreate.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def media_policies(self):
        """
        Gets the media_policies of this CrossPlatformPolicyCreate.
        Conditions and actions per media type

        :return: The media_policies of this CrossPlatformPolicyCreate.
        :rtype: CrossPlatformMediaPolicies
        """
        return self._media_policies

    @media_policies.setter
    def media_policies(self, media_policies):
        """
        Sets the media_policies of this CrossPlatformPolicyCreate.
        Conditions and actions per media type

        :param media_policies: The media_policies of this CrossPlatformPolicyCreate.
        :type: CrossPlatformMediaPolicies
        """
        
        self._media_policies = media_policies

    @property
    def conditions(self):
        """
        Gets the conditions of this CrossPlatformPolicyCreate.
        Conditions

        :return: The conditions of this CrossPlatformPolicyCreate.
        :rtype: PolicyConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this CrossPlatformPolicyCreate.
        Conditions

        :param conditions: The conditions of this CrossPlatformPolicyCreate.
        :type: PolicyConditions
        """
        
        self._conditions = conditions

    @property
    def actions(self):
        """
        Gets the actions of this CrossPlatformPolicyCreate.
        Actions

        :return: The actions of this CrossPlatformPolicyCreate.
        :rtype: CrossPlatformPolicyActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this CrossPlatformPolicyCreate.
        Actions

        :param actions: The actions of this CrossPlatformPolicyCreate.
        :type: CrossPlatformPolicyActions
        """
        
        self._actions = actions

    @property
    def policy_errors(self):
        """
        Gets the policy_errors of this CrossPlatformPolicyCreate.


        :return: The policy_errors of this CrossPlatformPolicyCreate.
        :rtype: PolicyErrors
        """
        return self._policy_errors

    @policy_errors.setter
    def policy_errors(self, policy_errors):
        """
        Sets the policy_errors of this CrossPlatformPolicyCreate.


        :param policy_errors: The policy_errors of this CrossPlatformPolicyCreate.
        :type: PolicyErrors
        """
        
        self._policy_errors = policy_errors

    @property
    def self_uri(self):
        """
        Gets the self_uri of this CrossPlatformPolicyCreate.
        The URI for this object

        :return: The self_uri of this CrossPlatformPolicyCreate.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this CrossPlatformPolicyCreate.
        The URI for this object

        :param self_uri: The self_uri of this CrossPlatformPolicyCreate.
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

