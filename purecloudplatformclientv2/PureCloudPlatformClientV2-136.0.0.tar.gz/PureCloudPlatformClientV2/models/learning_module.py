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

class LearningModule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LearningModule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'created_by': 'UserReference',
            'date_created': 'datetime',
            'modified_by': 'UserReference',
            'date_modified': 'datetime',
            'version': 'int',
            'external_id': 'str',
            'source': 'str',
            'rule': 'LearningModuleRule',
            'self_uri': 'str',
            'is_archived': 'bool',
            'is_published': 'bool',
            'description': 'str',
            'completion_time_in_days': 'int',
            'type': 'str',
            'inform_steps': 'list[LearningModuleInformStep]',
            'assessment_form': 'AssessmentForm',
            'summary_data': 'LearningModuleSummary'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'created_by': 'createdBy',
            'date_created': 'dateCreated',
            'modified_by': 'modifiedBy',
            'date_modified': 'dateModified',
            'version': 'version',
            'external_id': 'externalId',
            'source': 'source',
            'rule': 'rule',
            'self_uri': 'selfUri',
            'is_archived': 'isArchived',
            'is_published': 'isPublished',
            'description': 'description',
            'completion_time_in_days': 'completionTimeInDays',
            'type': 'type',
            'inform_steps': 'informSteps',
            'assessment_form': 'assessmentForm',
            'summary_data': 'summaryData'
        }

        self._id = None
        self._name = None
        self._created_by = None
        self._date_created = None
        self._modified_by = None
        self._date_modified = None
        self._version = None
        self._external_id = None
        self._source = None
        self._rule = None
        self._self_uri = None
        self._is_archived = None
        self._is_published = None
        self._description = None
        self._completion_time_in_days = None
        self._type = None
        self._inform_steps = None
        self._assessment_form = None
        self._summary_data = None

    @property
    def id(self):
        """
        Gets the id of this LearningModule.
        The globally unique identifier for the object.

        :return: The id of this LearningModule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LearningModule.
        The globally unique identifier for the object.

        :param id: The id of this LearningModule.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this LearningModule.
        The name of learning module

        :return: The name of this LearningModule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LearningModule.
        The name of learning module

        :param name: The name of this LearningModule.
        :type: str
        """
        
        self._name = name

    @property
    def created_by(self):
        """
        Gets the created_by of this LearningModule.
        The user who created learning module

        :return: The created_by of this LearningModule.
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this LearningModule.
        The user who created learning module

        :param created_by: The created_by of this LearningModule.
        :type: UserReference
        """
        
        self._created_by = created_by

    @property
    def date_created(self):
        """
        Gets the date_created of this LearningModule.
        The date/time learning module was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this LearningModule.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this LearningModule.
        The date/time learning module was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this LearningModule.
        :type: datetime
        """
        
        self._date_created = date_created

    @property
    def modified_by(self):
        """
        Gets the modified_by of this LearningModule.
        The user who modified learning module

        :return: The modified_by of this LearningModule.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """
        Sets the modified_by of this LearningModule.
        The user who modified learning module

        :param modified_by: The modified_by of this LearningModule.
        :type: UserReference
        """
        
        self._modified_by = modified_by

    @property
    def date_modified(self):
        """
        Gets the date_modified of this LearningModule.
        The date/time learning module was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this LearningModule.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """
        Sets the date_modified of this LearningModule.
        The date/time learning module was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this LearningModule.
        :type: datetime
        """
        
        self._date_modified = date_modified

    @property
    def version(self):
        """
        Gets the version of this LearningModule.
        The version of published learning module

        :return: The version of this LearningModule.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this LearningModule.
        The version of published learning module

        :param version: The version of this LearningModule.
        :type: int
        """
        
        self._version = version

    @property
    def external_id(self):
        """
        Gets the external_id of this LearningModule.
        The external ID of the learning module

        :return: The external_id of this LearningModule.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this LearningModule.
        The external ID of the learning module

        :param external_id: The external_id of this LearningModule.
        :type: str
        """
        
        self._external_id = external_id

    @property
    def source(self):
        """
        Gets the source of this LearningModule.
        The source of the learning module

        :return: The source of this LearningModule.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this LearningModule.
        The source of the learning module

        :param source: The source of this LearningModule.
        :type: str
        """
        allowed_values = ["UserCreated", "GenesysBeyond"]
        if source.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for source -> " + source)
            self._source = "outdated_sdk_version"
        else:
            self._source = source

    @property
    def rule(self):
        """
        Gets the rule of this LearningModule.
        The rule for learning module; read-only, and only populated when requested via expand param.

        :return: The rule of this LearningModule.
        :rtype: LearningModuleRule
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this LearningModule.
        The rule for learning module; read-only, and only populated when requested via expand param.

        :param rule: The rule of this LearningModule.
        :type: LearningModuleRule
        """
        
        self._rule = rule

    @property
    def self_uri(self):
        """
        Gets the self_uri of this LearningModule.
        The URI for this object

        :return: The self_uri of this LearningModule.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this LearningModule.
        The URI for this object

        :param self_uri: The self_uri of this LearningModule.
        :type: str
        """
        
        self._self_uri = self_uri

    @property
    def is_archived(self):
        """
        Gets the is_archived of this LearningModule.
        If true, learning module is archived

        :return: The is_archived of this LearningModule.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this LearningModule.
        If true, learning module is archived

        :param is_archived: The is_archived of this LearningModule.
        :type: bool
        """
        
        self._is_archived = is_archived

    @property
    def is_published(self):
        """
        Gets the is_published of this LearningModule.
        If true, learning module is published

        :return: The is_published of this LearningModule.
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """
        Sets the is_published of this LearningModule.
        If true, learning module is published

        :param is_published: The is_published of this LearningModule.
        :type: bool
        """
        
        self._is_published = is_published

    @property
    def description(self):
        """
        Gets the description of this LearningModule.
        The description of learning module

        :return: The description of this LearningModule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LearningModule.
        The description of learning module

        :param description: The description of this LearningModule.
        :type: str
        """
        
        self._description = description

    @property
    def completion_time_in_days(self):
        """
        Gets the completion_time_in_days of this LearningModule.
        The completion time of learning module in days

        :return: The completion_time_in_days of this LearningModule.
        :rtype: int
        """
        return self._completion_time_in_days

    @completion_time_in_days.setter
    def completion_time_in_days(self, completion_time_in_days):
        """
        Sets the completion_time_in_days of this LearningModule.
        The completion time of learning module in days

        :param completion_time_in_days: The completion_time_in_days of this LearningModule.
        :type: int
        """
        
        self._completion_time_in_days = completion_time_in_days

    @property
    def type(self):
        """
        Gets the type of this LearningModule.
        The type for the learning module

        :return: The type of this LearningModule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this LearningModule.
        The type for the learning module

        :param type: The type of this LearningModule.
        :type: str
        """
        allowed_values = ["Informational", "AssessedContent", "Assessment"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def inform_steps(self):
        """
        Gets the inform_steps of this LearningModule.
        The list of inform steps in a learning module

        :return: The inform_steps of this LearningModule.
        :rtype: list[LearningModuleInformStep]
        """
        return self._inform_steps

    @inform_steps.setter
    def inform_steps(self, inform_steps):
        """
        Sets the inform_steps of this LearningModule.
        The list of inform steps in a learning module

        :param inform_steps: The inform_steps of this LearningModule.
        :type: list[LearningModuleInformStep]
        """
        
        self._inform_steps = inform_steps

    @property
    def assessment_form(self):
        """
        Gets the assessment_form of this LearningModule.
        The assessment form for learning module

        :return: The assessment_form of this LearningModule.
        :rtype: AssessmentForm
        """
        return self._assessment_form

    @assessment_form.setter
    def assessment_form(self, assessment_form):
        """
        Sets the assessment_form of this LearningModule.
        The assessment form for learning module

        :param assessment_form: The assessment_form of this LearningModule.
        :type: AssessmentForm
        """
        
        self._assessment_form = assessment_form

    @property
    def summary_data(self):
        """
        Gets the summary_data of this LearningModule.
        The learning module summary data

        :return: The summary_data of this LearningModule.
        :rtype: LearningModuleSummary
        """
        return self._summary_data

    @summary_data.setter
    def summary_data(self, summary_data):
        """
        Sets the summary_data of this LearningModule.
        The learning module summary data

        :param summary_data: The summary_data of this LearningModule.
        :type: LearningModuleSummary
        """
        
        self._summary_data = summary_data

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

