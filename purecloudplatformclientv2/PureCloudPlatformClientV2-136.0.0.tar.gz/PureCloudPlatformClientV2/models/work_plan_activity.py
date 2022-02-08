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

class WorkPlanActivity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WorkPlanActivity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_code_id': 'str',
            'description': 'str',
            'length_minutes': 'int',
            'start_time_is_relative_to_shift_start': 'bool',
            'flexible_start_time': 'bool',
            'earliest_start_time_minutes': 'int',
            'latest_start_time_minutes': 'int',
            'exact_start_time_minutes': 'int',
            'start_time_increment_minutes': 'int',
            'counts_as_paid_time': 'bool',
            'counts_as_contiguous_work_time': 'bool',
            'minimum_length_from_shift_start_minutes': 'int',
            'minimum_length_from_shift_end_minutes': 'int',
            'id': 'str',
            'delete': 'bool',
            'validation_id': 'str'
        }

        self.attribute_map = {
            'activity_code_id': 'activityCodeId',
            'description': 'description',
            'length_minutes': 'lengthMinutes',
            'start_time_is_relative_to_shift_start': 'startTimeIsRelativeToShiftStart',
            'flexible_start_time': 'flexibleStartTime',
            'earliest_start_time_minutes': 'earliestStartTimeMinutes',
            'latest_start_time_minutes': 'latestStartTimeMinutes',
            'exact_start_time_minutes': 'exactStartTimeMinutes',
            'start_time_increment_minutes': 'startTimeIncrementMinutes',
            'counts_as_paid_time': 'countsAsPaidTime',
            'counts_as_contiguous_work_time': 'countsAsContiguousWorkTime',
            'minimum_length_from_shift_start_minutes': 'minimumLengthFromShiftStartMinutes',
            'minimum_length_from_shift_end_minutes': 'minimumLengthFromShiftEndMinutes',
            'id': 'id',
            'delete': 'delete',
            'validation_id': 'validationId'
        }

        self._activity_code_id = None
        self._description = None
        self._length_minutes = None
        self._start_time_is_relative_to_shift_start = None
        self._flexible_start_time = None
        self._earliest_start_time_minutes = None
        self._latest_start_time_minutes = None
        self._exact_start_time_minutes = None
        self._start_time_increment_minutes = None
        self._counts_as_paid_time = None
        self._counts_as_contiguous_work_time = None
        self._minimum_length_from_shift_start_minutes = None
        self._minimum_length_from_shift_end_minutes = None
        self._id = None
        self._delete = None
        self._validation_id = None

    @property
    def activity_code_id(self):
        """
        Gets the activity_code_id of this WorkPlanActivity.
        ID of the activity code associated with this activity

        :return: The activity_code_id of this WorkPlanActivity.
        :rtype: str
        """
        return self._activity_code_id

    @activity_code_id.setter
    def activity_code_id(self, activity_code_id):
        """
        Sets the activity_code_id of this WorkPlanActivity.
        ID of the activity code associated with this activity

        :param activity_code_id: The activity_code_id of this WorkPlanActivity.
        :type: str
        """
        
        self._activity_code_id = activity_code_id

    @property
    def description(self):
        """
        Gets the description of this WorkPlanActivity.
        Description of the activity

        :return: The description of this WorkPlanActivity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkPlanActivity.
        Description of the activity

        :param description: The description of this WorkPlanActivity.
        :type: str
        """
        
        self._description = description

    @property
    def length_minutes(self):
        """
        Gets the length_minutes of this WorkPlanActivity.
        Length of the activity in minutes

        :return: The length_minutes of this WorkPlanActivity.
        :rtype: int
        """
        return self._length_minutes

    @length_minutes.setter
    def length_minutes(self, length_minutes):
        """
        Sets the length_minutes of this WorkPlanActivity.
        Length of the activity in minutes

        :param length_minutes: The length_minutes of this WorkPlanActivity.
        :type: int
        """
        
        self._length_minutes = length_minutes

    @property
    def start_time_is_relative_to_shift_start(self):
        """
        Gets the start_time_is_relative_to_shift_start of this WorkPlanActivity.
        Whether the start time of the activity is relative to the start time of the shift it belongs to

        :return: The start_time_is_relative_to_shift_start of this WorkPlanActivity.
        :rtype: bool
        """
        return self._start_time_is_relative_to_shift_start

    @start_time_is_relative_to_shift_start.setter
    def start_time_is_relative_to_shift_start(self, start_time_is_relative_to_shift_start):
        """
        Sets the start_time_is_relative_to_shift_start of this WorkPlanActivity.
        Whether the start time of the activity is relative to the start time of the shift it belongs to

        :param start_time_is_relative_to_shift_start: The start_time_is_relative_to_shift_start of this WorkPlanActivity.
        :type: bool
        """
        
        self._start_time_is_relative_to_shift_start = start_time_is_relative_to_shift_start

    @property
    def flexible_start_time(self):
        """
        Gets the flexible_start_time of this WorkPlanActivity.
        Whether the start time of the activity is flexible

        :return: The flexible_start_time of this WorkPlanActivity.
        :rtype: bool
        """
        return self._flexible_start_time

    @flexible_start_time.setter
    def flexible_start_time(self, flexible_start_time):
        """
        Sets the flexible_start_time of this WorkPlanActivity.
        Whether the start time of the activity is flexible

        :param flexible_start_time: The flexible_start_time of this WorkPlanActivity.
        :type: bool
        """
        
        self._flexible_start_time = flexible_start_time

    @property
    def earliest_start_time_minutes(self):
        """
        Gets the earliest_start_time_minutes of this WorkPlanActivity.
        Earliest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :return: The earliest_start_time_minutes of this WorkPlanActivity.
        :rtype: int
        """
        return self._earliest_start_time_minutes

    @earliest_start_time_minutes.setter
    def earliest_start_time_minutes(self, earliest_start_time_minutes):
        """
        Sets the earliest_start_time_minutes of this WorkPlanActivity.
        Earliest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :param earliest_start_time_minutes: The earliest_start_time_minutes of this WorkPlanActivity.
        :type: int
        """
        
        self._earliest_start_time_minutes = earliest_start_time_minutes

    @property
    def latest_start_time_minutes(self):
        """
        Gets the latest_start_time_minutes of this WorkPlanActivity.
        Latest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :return: The latest_start_time_minutes of this WorkPlanActivity.
        :rtype: int
        """
        return self._latest_start_time_minutes

    @latest_start_time_minutes.setter
    def latest_start_time_minutes(self, latest_start_time_minutes):
        """
        Sets the latest_start_time_minutes of this WorkPlanActivity.
        Latest activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == true

        :param latest_start_time_minutes: The latest_start_time_minutes of this WorkPlanActivity.
        :type: int
        """
        
        self._latest_start_time_minutes = latest_start_time_minutes

    @property
    def exact_start_time_minutes(self):
        """
        Gets the exact_start_time_minutes of this WorkPlanActivity.
        Exact activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == false

        :return: The exact_start_time_minutes of this WorkPlanActivity.
        :rtype: int
        """
        return self._exact_start_time_minutes

    @exact_start_time_minutes.setter
    def exact_start_time_minutes(self, exact_start_time_minutes):
        """
        Sets the exact_start_time_minutes of this WorkPlanActivity.
        Exact activity start in offset minutes relative to shift start time if startTimeIsRelativeToShiftStart == true else its based on midnight. Used if flexibleStartTime == false

        :param exact_start_time_minutes: The exact_start_time_minutes of this WorkPlanActivity.
        :type: int
        """
        
        self._exact_start_time_minutes = exact_start_time_minutes

    @property
    def start_time_increment_minutes(self):
        """
        Gets the start_time_increment_minutes of this WorkPlanActivity.
        Increment in offset minutes that would contribute to different possible start times for the activity

        :return: The start_time_increment_minutes of this WorkPlanActivity.
        :rtype: int
        """
        return self._start_time_increment_minutes

    @start_time_increment_minutes.setter
    def start_time_increment_minutes(self, start_time_increment_minutes):
        """
        Sets the start_time_increment_minutes of this WorkPlanActivity.
        Increment in offset minutes that would contribute to different possible start times for the activity

        :param start_time_increment_minutes: The start_time_increment_minutes of this WorkPlanActivity.
        :type: int
        """
        
        self._start_time_increment_minutes = start_time_increment_minutes

    @property
    def counts_as_paid_time(self):
        """
        Gets the counts_as_paid_time of this WorkPlanActivity.
        Whether the activity is paid

        :return: The counts_as_paid_time of this WorkPlanActivity.
        :rtype: bool
        """
        return self._counts_as_paid_time

    @counts_as_paid_time.setter
    def counts_as_paid_time(self, counts_as_paid_time):
        """
        Sets the counts_as_paid_time of this WorkPlanActivity.
        Whether the activity is paid

        :param counts_as_paid_time: The counts_as_paid_time of this WorkPlanActivity.
        :type: bool
        """
        
        self._counts_as_paid_time = counts_as_paid_time

    @property
    def counts_as_contiguous_work_time(self):
        """
        Gets the counts_as_contiguous_work_time of this WorkPlanActivity.
        Whether the activity duration is counted towards contiguous work time

        :return: The counts_as_contiguous_work_time of this WorkPlanActivity.
        :rtype: bool
        """
        return self._counts_as_contiguous_work_time

    @counts_as_contiguous_work_time.setter
    def counts_as_contiguous_work_time(self, counts_as_contiguous_work_time):
        """
        Sets the counts_as_contiguous_work_time of this WorkPlanActivity.
        Whether the activity duration is counted towards contiguous work time

        :param counts_as_contiguous_work_time: The counts_as_contiguous_work_time of this WorkPlanActivity.
        :type: bool
        """
        
        self._counts_as_contiguous_work_time = counts_as_contiguous_work_time

    @property
    def minimum_length_from_shift_start_minutes(self):
        """
        Gets the minimum_length_from_shift_start_minutes of this WorkPlanActivity.
        The minimum duration between shift start and shift item (e.g., break or meal) start in minutes

        :return: The minimum_length_from_shift_start_minutes of this WorkPlanActivity.
        :rtype: int
        """
        return self._minimum_length_from_shift_start_minutes

    @minimum_length_from_shift_start_minutes.setter
    def minimum_length_from_shift_start_minutes(self, minimum_length_from_shift_start_minutes):
        """
        Sets the minimum_length_from_shift_start_minutes of this WorkPlanActivity.
        The minimum duration between shift start and shift item (e.g., break or meal) start in minutes

        :param minimum_length_from_shift_start_minutes: The minimum_length_from_shift_start_minutes of this WorkPlanActivity.
        :type: int
        """
        
        self._minimum_length_from_shift_start_minutes = minimum_length_from_shift_start_minutes

    @property
    def minimum_length_from_shift_end_minutes(self):
        """
        Gets the minimum_length_from_shift_end_minutes of this WorkPlanActivity.
        The minimum duration between shift item (e.g., break or meal) end and shift end in minutes

        :return: The minimum_length_from_shift_end_minutes of this WorkPlanActivity.
        :rtype: int
        """
        return self._minimum_length_from_shift_end_minutes

    @minimum_length_from_shift_end_minutes.setter
    def minimum_length_from_shift_end_minutes(self, minimum_length_from_shift_end_minutes):
        """
        Sets the minimum_length_from_shift_end_minutes of this WorkPlanActivity.
        The minimum duration between shift item (e.g., break or meal) end and shift end in minutes

        :param minimum_length_from_shift_end_minutes: The minimum_length_from_shift_end_minutes of this WorkPlanActivity.
        :type: int
        """
        
        self._minimum_length_from_shift_end_minutes = minimum_length_from_shift_end_minutes

    @property
    def id(self):
        """
        Gets the id of this WorkPlanActivity.
        ID of the activity. This is required only for the case of updating an existing activity

        :return: The id of this WorkPlanActivity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkPlanActivity.
        ID of the activity. This is required only for the case of updating an existing activity

        :param id: The id of this WorkPlanActivity.
        :type: str
        """
        
        self._id = id

    @property
    def delete(self):
        """
        Gets the delete of this WorkPlanActivity.
        If marked true for updating an existing activity, the activity will be permanently deleted

        :return: The delete of this WorkPlanActivity.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """
        Sets the delete of this WorkPlanActivity.
        If marked true for updating an existing activity, the activity will be permanently deleted

        :param delete: The delete of this WorkPlanActivity.
        :type: bool
        """
        
        self._delete = delete

    @property
    def validation_id(self):
        """
        Gets the validation_id of this WorkPlanActivity.
        ID of the activity in the context of work plan validation

        :return: The validation_id of this WorkPlanActivity.
        :rtype: str
        """
        return self._validation_id

    @validation_id.setter
    def validation_id(self, validation_id):
        """
        Sets the validation_id of this WorkPlanActivity.
        ID of the activity in the context of work plan validation

        :param validation_id: The validation_id of this WorkPlanActivity.
        :type: str
        """
        
        self._validation_id = validation_id

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

