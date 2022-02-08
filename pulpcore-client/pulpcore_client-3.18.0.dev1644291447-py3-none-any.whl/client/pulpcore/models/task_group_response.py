# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class TaskGroupResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pulp_href': 'str',
        'description': 'str',
        'all_tasks_dispatched': 'bool',
        'waiting': 'int',
        'skipped': 'int',
        'running': 'int',
        'completed': 'int',
        'canceled': 'int',
        'failed': 'int',
        'canceling': 'int',
        'group_progress_reports': 'list[GroupProgressReportResponse]',
        'tasks': 'list[MinimalTaskResponse]'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'description': 'description',
        'all_tasks_dispatched': 'all_tasks_dispatched',
        'waiting': 'waiting',
        'skipped': 'skipped',
        'running': 'running',
        'completed': 'completed',
        'canceled': 'canceled',
        'failed': 'failed',
        'canceling': 'canceling',
        'group_progress_reports': 'group_progress_reports',
        'tasks': 'tasks'
    }

    def __init__(self, pulp_href=None, description=None, all_tasks_dispatched=None, waiting=None, skipped=None, running=None, completed=None, canceled=None, failed=None, canceling=None, group_progress_reports=None, tasks=None, local_vars_configuration=None):  # noqa: E501
        """TaskGroupResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._description = None
        self._all_tasks_dispatched = None
        self._waiting = None
        self._skipped = None
        self._running = None
        self._completed = None
        self._canceled = None
        self._failed = None
        self._canceling = None
        self._group_progress_reports = None
        self._tasks = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        self.description = description
        self.all_tasks_dispatched = all_tasks_dispatched
        if waiting is not None:
            self.waiting = waiting
        if skipped is not None:
            self.skipped = skipped
        if running is not None:
            self.running = running
        if completed is not None:
            self.completed = completed
        if canceled is not None:
            self.canceled = canceled
        if failed is not None:
            self.failed = failed
        if canceling is not None:
            self.canceling = canceling
        if group_progress_reports is not None:
            self.group_progress_reports = group_progress_reports
        if tasks is not None:
            self.tasks = tasks

    @property
    def pulp_href(self):
        """Gets the pulp_href of this TaskGroupResponse.  # noqa: E501


        :return: The pulp_href of this TaskGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this TaskGroupResponse.


        :param pulp_href: The pulp_href of this TaskGroupResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def description(self):
        """Gets the description of this TaskGroupResponse.  # noqa: E501

        A description of the task group.  # noqa: E501

        :return: The description of this TaskGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskGroupResponse.

        A description of the task group.  # noqa: E501

        :param description: The description of this TaskGroupResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def all_tasks_dispatched(self):
        """Gets the all_tasks_dispatched of this TaskGroupResponse.  # noqa: E501

        Whether all tasks have been spawned for this task group.  # noqa: E501

        :return: The all_tasks_dispatched of this TaskGroupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._all_tasks_dispatched

    @all_tasks_dispatched.setter
    def all_tasks_dispatched(self, all_tasks_dispatched):
        """Sets the all_tasks_dispatched of this TaskGroupResponse.

        Whether all tasks have been spawned for this task group.  # noqa: E501

        :param all_tasks_dispatched: The all_tasks_dispatched of this TaskGroupResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and all_tasks_dispatched is None:  # noqa: E501
            raise ValueError("Invalid value for `all_tasks_dispatched`, must not be `None`")  # noqa: E501

        self._all_tasks_dispatched = all_tasks_dispatched

    @property
    def waiting(self):
        """Gets the waiting of this TaskGroupResponse.  # noqa: E501

        Number of tasks in the 'waiting' state  # noqa: E501

        :return: The waiting of this TaskGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this TaskGroupResponse.

        Number of tasks in the 'waiting' state  # noqa: E501

        :param waiting: The waiting of this TaskGroupResponse.  # noqa: E501
        :type: int
        """

        self._waiting = waiting

    @property
    def skipped(self):
        """Gets the skipped of this TaskGroupResponse.  # noqa: E501

        Number of tasks in the 'skipped' state  # noqa: E501

        :return: The skipped of this TaskGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._skipped

    @skipped.setter
    def skipped(self, skipped):
        """Sets the skipped of this TaskGroupResponse.

        Number of tasks in the 'skipped' state  # noqa: E501

        :param skipped: The skipped of this TaskGroupResponse.  # noqa: E501
        :type: int
        """

        self._skipped = skipped

    @property
    def running(self):
        """Gets the running of this TaskGroupResponse.  # noqa: E501

        Number of tasks in the 'running' state  # noqa: E501

        :return: The running of this TaskGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this TaskGroupResponse.

        Number of tasks in the 'running' state  # noqa: E501

        :param running: The running of this TaskGroupResponse.  # noqa: E501
        :type: int
        """

        self._running = running

    @property
    def completed(self):
        """Gets the completed of this TaskGroupResponse.  # noqa: E501

        Number of tasks in the 'completed' state  # noqa: E501

        :return: The completed of this TaskGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this TaskGroupResponse.

        Number of tasks in the 'completed' state  # noqa: E501

        :param completed: The completed of this TaskGroupResponse.  # noqa: E501
        :type: int
        """

        self._completed = completed

    @property
    def canceled(self):
        """Gets the canceled of this TaskGroupResponse.  # noqa: E501

        Number of tasks in the 'canceled' state  # noqa: E501

        :return: The canceled of this TaskGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """Sets the canceled of this TaskGroupResponse.

        Number of tasks in the 'canceled' state  # noqa: E501

        :param canceled: The canceled of this TaskGroupResponse.  # noqa: E501
        :type: int
        """

        self._canceled = canceled

    @property
    def failed(self):
        """Gets the failed of this TaskGroupResponse.  # noqa: E501

        Number of tasks in the 'failed' state  # noqa: E501

        :return: The failed of this TaskGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this TaskGroupResponse.

        Number of tasks in the 'failed' state  # noqa: E501

        :param failed: The failed of this TaskGroupResponse.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def canceling(self):
        """Gets the canceling of this TaskGroupResponse.  # noqa: E501

        Number of tasks in the 'canceling' state  # noqa: E501

        :return: The canceling of this TaskGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._canceling

    @canceling.setter
    def canceling(self, canceling):
        """Sets the canceling of this TaskGroupResponse.

        Number of tasks in the 'canceling' state  # noqa: E501

        :param canceling: The canceling of this TaskGroupResponse.  # noqa: E501
        :type: int
        """

        self._canceling = canceling

    @property
    def group_progress_reports(self):
        """Gets the group_progress_reports of this TaskGroupResponse.  # noqa: E501


        :return: The group_progress_reports of this TaskGroupResponse.  # noqa: E501
        :rtype: list[GroupProgressReportResponse]
        """
        return self._group_progress_reports

    @group_progress_reports.setter
    def group_progress_reports(self, group_progress_reports):
        """Sets the group_progress_reports of this TaskGroupResponse.


        :param group_progress_reports: The group_progress_reports of this TaskGroupResponse.  # noqa: E501
        :type: list[GroupProgressReportResponse]
        """

        self._group_progress_reports = group_progress_reports

    @property
    def tasks(self):
        """Gets the tasks of this TaskGroupResponse.  # noqa: E501


        :return: The tasks of this TaskGroupResponse.  # noqa: E501
        :rtype: list[MinimalTaskResponse]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this TaskGroupResponse.


        :param tasks: The tasks of this TaskGroupResponse.  # noqa: E501
        :type: list[MinimalTaskResponse]
        """

        self._tasks = tasks

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskGroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskGroupResponse):
            return True

        return self.to_dict() != other.to_dict()
