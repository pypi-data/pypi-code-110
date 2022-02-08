#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.15.0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from polyaxon_sdk.configuration import Configuration


class V1ProjectVersion(object):
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
        'uuid': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'owner': 'str',
        'project': 'str',
        'connection': 'str',
        'run': 'str',
        'artifacts': 'list[str]',
        'meta_info': 'object',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'stage': 'V1Stages',
        'kind': 'V1ProjectVersionKind',
        'stage_conditions': 'list[V1StageCondition]',
        'content': 'str',
        'state': 'str',
        'role': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'owner': 'owner',
        'project': 'project',
        'connection': 'connection',
        'run': 'run',
        'artifacts': 'artifacts',
        'meta_info': 'meta_info',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'stage': 'stage',
        'kind': 'kind',
        'stage_conditions': 'stage_conditions',
        'content': 'content',
        'state': 'state',
        'role': 'role'
    }

    def __init__(self, uuid=None, name=None, description=None, tags=None, owner=None, project=None, connection=None, run=None, artifacts=None, meta_info=None, created_at=None, updated_at=None, stage=None, kind=None, stage_conditions=None, content=None, state=None, role=None, local_vars_configuration=None):  # noqa: E501
        """V1ProjectVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._name = None
        self._description = None
        self._tags = None
        self._owner = None
        self._project = None
        self._connection = None
        self._run = None
        self._artifacts = None
        self._meta_info = None
        self._created_at = None
        self._updated_at = None
        self._stage = None
        self._kind = None
        self._stage_conditions = None
        self._content = None
        self._state = None
        self._role = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if owner is not None:
            self.owner = owner
        if project is not None:
            self.project = project
        if connection is not None:
            self.connection = connection
        if run is not None:
            self.run = run
        if artifacts is not None:
            self.artifacts = artifacts
        if meta_info is not None:
            self.meta_info = meta_info
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if stage is not None:
            self.stage = stage
        if kind is not None:
            self.kind = kind
        if stage_conditions is not None:
            self.stage_conditions = stage_conditions
        if content is not None:
            self.content = content
        if state is not None:
            self.state = state
        if role is not None:
            self.role = role

    @property
    def uuid(self):
        """Gets the uuid of this V1ProjectVersion.  # noqa: E501


        :return: The uuid of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this V1ProjectVersion.


        :param uuid: The uuid of this V1ProjectVersion.  # noqa: E501
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this V1ProjectVersion.  # noqa: E501


        :return: The name of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ProjectVersion.


        :param name: The name of this V1ProjectVersion.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this V1ProjectVersion.  # noqa: E501


        :return: The description of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ProjectVersion.


        :param description: The description of this V1ProjectVersion.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this V1ProjectVersion.  # noqa: E501


        :return: The tags of this V1ProjectVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1ProjectVersion.


        :param tags: The tags of this V1ProjectVersion.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def owner(self):
        """Gets the owner of this V1ProjectVersion.  # noqa: E501


        :return: The owner of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this V1ProjectVersion.


        :param owner: The owner of this V1ProjectVersion.  # noqa: E501
        :type owner: str
        """

        self._owner = owner

    @property
    def project(self):
        """Gets the project of this V1ProjectVersion.  # noqa: E501


        :return: The project of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1ProjectVersion.


        :param project: The project of this V1ProjectVersion.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def connection(self):
        """Gets the connection of this V1ProjectVersion.  # noqa: E501


        :return: The connection of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this V1ProjectVersion.


        :param connection: The connection of this V1ProjectVersion.  # noqa: E501
        :type connection: str
        """

        self._connection = connection

    @property
    def run(self):
        """Gets the run of this V1ProjectVersion.  # noqa: E501


        :return: The run of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this V1ProjectVersion.


        :param run: The run of this V1ProjectVersion.  # noqa: E501
        :type run: str
        """

        self._run = run

    @property
    def artifacts(self):
        """Gets the artifacts of this V1ProjectVersion.  # noqa: E501


        :return: The artifacts of this V1ProjectVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this V1ProjectVersion.


        :param artifacts: The artifacts of this V1ProjectVersion.  # noqa: E501
        :type artifacts: list[str]
        """

        self._artifacts = artifacts

    @property
    def meta_info(self):
        """Gets the meta_info of this V1ProjectVersion.  # noqa: E501


        :return: The meta_info of this V1ProjectVersion.  # noqa: E501
        :rtype: object
        """
        return self._meta_info

    @meta_info.setter
    def meta_info(self, meta_info):
        """Sets the meta_info of this V1ProjectVersion.


        :param meta_info: The meta_info of this V1ProjectVersion.  # noqa: E501
        :type meta_info: object
        """

        self._meta_info = meta_info

    @property
    def created_at(self):
        """Gets the created_at of this V1ProjectVersion.  # noqa: E501


        :return: The created_at of this V1ProjectVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1ProjectVersion.


        :param created_at: The created_at of this V1ProjectVersion.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this V1ProjectVersion.  # noqa: E501


        :return: The updated_at of this V1ProjectVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V1ProjectVersion.


        :param updated_at: The updated_at of this V1ProjectVersion.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def stage(self):
        """Gets the stage of this V1ProjectVersion.  # noqa: E501


        :return: The stage of this V1ProjectVersion.  # noqa: E501
        :rtype: V1Stages
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this V1ProjectVersion.


        :param stage: The stage of this V1ProjectVersion.  # noqa: E501
        :type stage: V1Stages
        """

        self._stage = stage

    @property
    def kind(self):
        """Gets the kind of this V1ProjectVersion.  # noqa: E501


        :return: The kind of this V1ProjectVersion.  # noqa: E501
        :rtype: V1ProjectVersionKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1ProjectVersion.


        :param kind: The kind of this V1ProjectVersion.  # noqa: E501
        :type kind: V1ProjectVersionKind
        """

        self._kind = kind

    @property
    def stage_conditions(self):
        """Gets the stage_conditions of this V1ProjectVersion.  # noqa: E501


        :return: The stage_conditions of this V1ProjectVersion.  # noqa: E501
        :rtype: list[V1StageCondition]
        """
        return self._stage_conditions

    @stage_conditions.setter
    def stage_conditions(self, stage_conditions):
        """Sets the stage_conditions of this V1ProjectVersion.


        :param stage_conditions: The stage_conditions of this V1ProjectVersion.  # noqa: E501
        :type stage_conditions: list[V1StageCondition]
        """

        self._stage_conditions = stage_conditions

    @property
    def content(self):
        """Gets the content of this V1ProjectVersion.  # noqa: E501


        :return: The content of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this V1ProjectVersion.


        :param content: The content of this V1ProjectVersion.  # noqa: E501
        :type content: str
        """

        self._content = content

    @property
    def state(self):
        """Gets the state of this V1ProjectVersion.  # noqa: E501


        :return: The state of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1ProjectVersion.


        :param state: The state of this V1ProjectVersion.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def role(self):
        """Gets the role of this V1ProjectVersion.  # noqa: E501


        :return: The role of this V1ProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this V1ProjectVersion.


        :param role: The role of this V1ProjectVersion.  # noqa: E501
        :type role: str
        """

        self._role = role

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ProjectVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ProjectVersion):
            return True

        return self.to_dict() != other.to_dict()
