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

class SurveyQuestionScore(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SurveyQuestionScore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'question_id': 'str',
            'answer_id': 'str',
            'score': 'int',
            'marked_na': 'bool',
            'nps_score': 'int',
            'nps_text_answer': 'str',
            'free_text_answer': 'str'
        }

        self.attribute_map = {
            'question_id': 'questionId',
            'answer_id': 'answerId',
            'score': 'score',
            'marked_na': 'markedNA',
            'nps_score': 'npsScore',
            'nps_text_answer': 'npsTextAnswer',
            'free_text_answer': 'freeTextAnswer'
        }

        self._question_id = None
        self._answer_id = None
        self._score = None
        self._marked_na = None
        self._nps_score = None
        self._nps_text_answer = None
        self._free_text_answer = None

    @property
    def question_id(self):
        """
        Gets the question_id of this SurveyQuestionScore.


        :return: The question_id of this SurveyQuestionScore.
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """
        Sets the question_id of this SurveyQuestionScore.


        :param question_id: The question_id of this SurveyQuestionScore.
        :type: str
        """
        
        self._question_id = question_id

    @property
    def answer_id(self):
        """
        Gets the answer_id of this SurveyQuestionScore.


        :return: The answer_id of this SurveyQuestionScore.
        :rtype: str
        """
        return self._answer_id

    @answer_id.setter
    def answer_id(self, answer_id):
        """
        Sets the answer_id of this SurveyQuestionScore.


        :param answer_id: The answer_id of this SurveyQuestionScore.
        :type: str
        """
        
        self._answer_id = answer_id

    @property
    def score(self):
        """
        Gets the score of this SurveyQuestionScore.
        Unweighted score of the question

        :return: The score of this SurveyQuestionScore.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this SurveyQuestionScore.
        Unweighted score of the question

        :param score: The score of this SurveyQuestionScore.
        :type: int
        """
        
        self._score = score

    @property
    def marked_na(self):
        """
        Gets the marked_na of this SurveyQuestionScore.


        :return: The marked_na of this SurveyQuestionScore.
        :rtype: bool
        """
        return self._marked_na

    @marked_na.setter
    def marked_na(self, marked_na):
        """
        Sets the marked_na of this SurveyQuestionScore.


        :param marked_na: The marked_na of this SurveyQuestionScore.
        :type: bool
        """
        
        self._marked_na = marked_na

    @property
    def nps_score(self):
        """
        Gets the nps_score of this SurveyQuestionScore.


        :return: The nps_score of this SurveyQuestionScore.
        :rtype: int
        """
        return self._nps_score

    @nps_score.setter
    def nps_score(self, nps_score):
        """
        Sets the nps_score of this SurveyQuestionScore.


        :param nps_score: The nps_score of this SurveyQuestionScore.
        :type: int
        """
        
        self._nps_score = nps_score

    @property
    def nps_text_answer(self):
        """
        Gets the nps_text_answer of this SurveyQuestionScore.


        :return: The nps_text_answer of this SurveyQuestionScore.
        :rtype: str
        """
        return self._nps_text_answer

    @nps_text_answer.setter
    def nps_text_answer(self, nps_text_answer):
        """
        Sets the nps_text_answer of this SurveyQuestionScore.


        :param nps_text_answer: The nps_text_answer of this SurveyQuestionScore.
        :type: str
        """
        
        self._nps_text_answer = nps_text_answer

    @property
    def free_text_answer(self):
        """
        Gets the free_text_answer of this SurveyQuestionScore.


        :return: The free_text_answer of this SurveyQuestionScore.
        :rtype: str
        """
        return self._free_text_answer

    @free_text_answer.setter
    def free_text_answer(self, free_text_answer):
        """
        Sets the free_text_answer of this SurveyQuestionScore.


        :param free_text_answer: The free_text_answer of this SurveyQuestionScore.
        :type: str
        """
        
        self._free_text_answer = free_text_answer

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

