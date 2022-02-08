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

class WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'week_date': 'str',
            'creation_method': 'str',
            'description': 'str',
            'legacy': 'bool',
            'reference_start_date': 'datetime',
            'source_days': 'list[WfmBuShortTermForecastGenerateProgressTopicForecastSourceDayPointer]',
            'modifications': 'list[WfmBuShortTermForecastGenerateProgressTopicBuForecastModification]',
            'time_zone': 'str',
            'planning_groups_version': 'int',
            'week_count': 'int',
            'metadata': 'WfmBuShortTermForecastGenerateProgressTopicWfmVersionedEntityMetadata',
            'can_use_for_scheduling': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'week_date': 'weekDate',
            'creation_method': 'creationMethod',
            'description': 'description',
            'legacy': 'legacy',
            'reference_start_date': 'referenceStartDate',
            'source_days': 'sourceDays',
            'modifications': 'modifications',
            'time_zone': 'timeZone',
            'planning_groups_version': 'planningGroupsVersion',
            'week_count': 'weekCount',
            'metadata': 'metadata',
            'can_use_for_scheduling': 'canUseForScheduling'
        }

        self._id = None
        self._week_date = None
        self._creation_method = None
        self._description = None
        self._legacy = None
        self._reference_start_date = None
        self._source_days = None
        self._modifications = None
        self._time_zone = None
        self._planning_groups_version = None
        self._week_count = None
        self._metadata = None
        self._can_use_for_scheduling = None

    @property
    def id(self):
        """
        Gets the id of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The id of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param id: The id of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: str
        """
        
        self._id = id

    @property
    def week_date(self):
        """
        Gets the week_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The week_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: str
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date):
        """
        Sets the week_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param week_date: The week_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: str
        """
        
        self._week_date = week_date

    @property
    def creation_method(self):
        """
        Gets the creation_method of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The creation_method of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: str
        """
        return self._creation_method

    @creation_method.setter
    def creation_method(self, creation_method):
        """
        Sets the creation_method of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param creation_method: The creation_method of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: str
        """
        allowed_values = ["Import", "ImportedHistoricalWeightedAverage", "HistoricalWeightedAverage", "Advanced"]
        if creation_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for creation_method -> " + creation_method)
            self._creation_method = "outdated_sdk_version"
        else:
            self._creation_method = creation_method

    @property
    def description(self):
        """
        Gets the description of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The description of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param description: The description of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: str
        """
        
        self._description = description

    @property
    def legacy(self):
        """
        Gets the legacy of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The legacy of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: bool
        """
        return self._legacy

    @legacy.setter
    def legacy(self, legacy):
        """
        Sets the legacy of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param legacy: The legacy of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: bool
        """
        
        self._legacy = legacy

    @property
    def reference_start_date(self):
        """
        Gets the reference_start_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The reference_start_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: datetime
        """
        return self._reference_start_date

    @reference_start_date.setter
    def reference_start_date(self, reference_start_date):
        """
        Sets the reference_start_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param reference_start_date: The reference_start_date of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: datetime
        """
        
        self._reference_start_date = reference_start_date

    @property
    def source_days(self):
        """
        Gets the source_days of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The source_days of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: list[WfmBuShortTermForecastGenerateProgressTopicForecastSourceDayPointer]
        """
        return self._source_days

    @source_days.setter
    def source_days(self, source_days):
        """
        Sets the source_days of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param source_days: The source_days of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: list[WfmBuShortTermForecastGenerateProgressTopicForecastSourceDayPointer]
        """
        
        self._source_days = source_days

    @property
    def modifications(self):
        """
        Gets the modifications of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The modifications of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: list[WfmBuShortTermForecastGenerateProgressTopicBuForecastModification]
        """
        return self._modifications

    @modifications.setter
    def modifications(self, modifications):
        """
        Sets the modifications of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param modifications: The modifications of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: list[WfmBuShortTermForecastGenerateProgressTopicBuForecastModification]
        """
        
        self._modifications = modifications

    @property
    def time_zone(self):
        """
        Gets the time_zone of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The time_zone of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param time_zone: The time_zone of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: str
        """
        
        self._time_zone = time_zone

    @property
    def planning_groups_version(self):
        """
        Gets the planning_groups_version of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The planning_groups_version of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: int
        """
        return self._planning_groups_version

    @planning_groups_version.setter
    def planning_groups_version(self, planning_groups_version):
        """
        Sets the planning_groups_version of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param planning_groups_version: The planning_groups_version of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: int
        """
        
        self._planning_groups_version = planning_groups_version

    @property
    def week_count(self):
        """
        Gets the week_count of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The week_count of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: int
        """
        return self._week_count

    @week_count.setter
    def week_count(self, week_count):
        """
        Sets the week_count of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param week_count: The week_count of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: int
        """
        
        self._week_count = week_count

    @property
    def metadata(self):
        """
        Gets the metadata of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The metadata of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: WfmBuShortTermForecastGenerateProgressTopicWfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param metadata: The metadata of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: WfmBuShortTermForecastGenerateProgressTopicWfmVersionedEntityMetadata
        """
        
        self._metadata = metadata

    @property
    def can_use_for_scheduling(self):
        """
        Gets the can_use_for_scheduling of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :return: The can_use_for_scheduling of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :rtype: bool
        """
        return self._can_use_for_scheduling

    @can_use_for_scheduling.setter
    def can_use_for_scheduling(self, can_use_for_scheduling):
        """
        Sets the can_use_for_scheduling of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.


        :param can_use_for_scheduling: The can_use_for_scheduling of this WfmBuShortTermForecastGenerateProgressTopicBuShortTermForecast.
        :type: bool
        """
        
        self._can_use_for_scheduling = can_use_for_scheduling

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

