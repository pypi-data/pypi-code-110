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

class ConversationMetrics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConversationMetrics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'conversation': 'AddressableEntityRef',
            'sentiment_score': 'float',
            'sentiment_trend': 'float',
            'sentiment_trend_class': 'str',
            'participant_metrics': 'ParticipantMetrics'
        }

        self.attribute_map = {
            'conversation': 'conversation',
            'sentiment_score': 'sentimentScore',
            'sentiment_trend': 'sentimentTrend',
            'sentiment_trend_class': 'sentimentTrendClass',
            'participant_metrics': 'participantMetrics'
        }

        self._conversation = None
        self._sentiment_score = None
        self._sentiment_trend = None
        self._sentiment_trend_class = None
        self._participant_metrics = None

    @property
    def conversation(self):
        """
        Gets the conversation of this ConversationMetrics.
        The Conversation Reference

        :return: The conversation of this ConversationMetrics.
        :rtype: AddressableEntityRef
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """
        Sets the conversation of this ConversationMetrics.
        The Conversation Reference

        :param conversation: The conversation of this ConversationMetrics.
        :type: AddressableEntityRef
        """
        
        self._conversation = conversation

    @property
    def sentiment_score(self):
        """
        Gets the sentiment_score of this ConversationMetrics.
        The Sentiment Score

        :return: The sentiment_score of this ConversationMetrics.
        :rtype: float
        """
        return self._sentiment_score

    @sentiment_score.setter
    def sentiment_score(self, sentiment_score):
        """
        Sets the sentiment_score of this ConversationMetrics.
        The Sentiment Score

        :param sentiment_score: The sentiment_score of this ConversationMetrics.
        :type: float
        """
        
        self._sentiment_score = sentiment_score

    @property
    def sentiment_trend(self):
        """
        Gets the sentiment_trend of this ConversationMetrics.
        The Sentiment Trend

        :return: The sentiment_trend of this ConversationMetrics.
        :rtype: float
        """
        return self._sentiment_trend

    @sentiment_trend.setter
    def sentiment_trend(self, sentiment_trend):
        """
        Sets the sentiment_trend of this ConversationMetrics.
        The Sentiment Trend

        :param sentiment_trend: The sentiment_trend of this ConversationMetrics.
        :type: float
        """
        
        self._sentiment_trend = sentiment_trend

    @property
    def sentiment_trend_class(self):
        """
        Gets the sentiment_trend_class of this ConversationMetrics.
        The Sentiment Trend Class

        :return: The sentiment_trend_class of this ConversationMetrics.
        :rtype: str
        """
        return self._sentiment_trend_class

    @sentiment_trend_class.setter
    def sentiment_trend_class(self, sentiment_trend_class):
        """
        Sets the sentiment_trend_class of this ConversationMetrics.
        The Sentiment Trend Class

        :param sentiment_trend_class: The sentiment_trend_class of this ConversationMetrics.
        :type: str
        """
        allowed_values = ["NotCalculated", "Declining", "SlightlyDeclining", "NoChange", "SlightlyImproving", "Improving"]
        if sentiment_trend_class.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for sentiment_trend_class -> " + sentiment_trend_class)
            self._sentiment_trend_class = "outdated_sdk_version"
        else:
            self._sentiment_trend_class = sentiment_trend_class

    @property
    def participant_metrics(self):
        """
        Gets the participant_metrics of this ConversationMetrics.
        The Participant Metrics

        :return: The participant_metrics of this ConversationMetrics.
        :rtype: ParticipantMetrics
        """
        return self._participant_metrics

    @participant_metrics.setter
    def participant_metrics(self, participant_metrics):
        """
        Sets the participant_metrics of this ConversationMetrics.
        The Participant Metrics

        :param participant_metrics: The participant_metrics of this ConversationMetrics.
        :type: ParticipantMetrics
        """
        
        self._participant_metrics = participant_metrics

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

