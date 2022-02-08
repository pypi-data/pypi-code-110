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

class OutcomeEventScore(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OutcomeEventScore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'outcome': 'AddressableEntityRef',
            'session_max_probability': 'float',
            'probability': 'float'
        }

        self.attribute_map = {
            'outcome': 'outcome',
            'session_max_probability': 'sessionMaxProbability',
            'probability': 'probability'
        }

        self._outcome = None
        self._session_max_probability = None
        self._probability = None

    @property
    def outcome(self):
        """
        Gets the outcome of this OutcomeEventScore.
        The outcome that the score was calculated for.

        :return: The outcome of this OutcomeEventScore.
        :rtype: AddressableEntityRef
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """
        Sets the outcome of this OutcomeEventScore.
        The outcome that the score was calculated for.

        :param outcome: The outcome of this OutcomeEventScore.
        :type: AddressableEntityRef
        """
        
        self._outcome = outcome

    @property
    def session_max_probability(self):
        """
        Gets the session_max_probability of this OutcomeEventScore.
        Represents the max probability reached in the session.

        :return: The session_max_probability of this OutcomeEventScore.
        :rtype: float
        """
        return self._session_max_probability

    @session_max_probability.setter
    def session_max_probability(self, session_max_probability):
        """
        Sets the session_max_probability of this OutcomeEventScore.
        Represents the max probability reached in the session.

        :param session_max_probability: The session_max_probability of this OutcomeEventScore.
        :type: float
        """
        
        self._session_max_probability = session_max_probability

    @property
    def probability(self):
        """
        Gets the probability of this OutcomeEventScore.
        Represents the likelihood of a customer reaching or achieving a given outcome.

        :return: The probability of this OutcomeEventScore.
        :rtype: float
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """
        Sets the probability of this OutcomeEventScore.
        Represents the likelihood of a customer reaching or achieving a given outcome.

        :param probability: The probability of this OutcomeEventScore.
        :type: float
        """
        
        self._probability = probability

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

