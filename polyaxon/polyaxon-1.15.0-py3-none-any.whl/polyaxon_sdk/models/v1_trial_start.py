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


class V1TrialStart(object):
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
        'name': 'str',
        'email': 'str',
        'organization': 'str',
        'plan': 'str',
        'seats': 'int',
        'details': 'object'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'organization': 'organization',
        'plan': 'plan',
        'seats': 'seats',
        'details': 'details'
    }

    def __init__(self, name=None, email=None, organization=None, plan=None, seats=None, details=None, local_vars_configuration=None):  # noqa: E501
        """V1TrialStart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._email = None
        self._organization = None
        self._plan = None
        self._seats = None
        self._details = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if organization is not None:
            self.organization = organization
        if plan is not None:
            self.plan = plan
        if seats is not None:
            self.seats = seats
        if details is not None:
            self.details = details

    @property
    def name(self):
        """Gets the name of this V1TrialStart.  # noqa: E501


        :return: The name of this V1TrialStart.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1TrialStart.


        :param name: The name of this V1TrialStart.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this V1TrialStart.  # noqa: E501


        :return: The email of this V1TrialStart.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this V1TrialStart.


        :param email: The email of this V1TrialStart.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def organization(self):
        """Gets the organization of this V1TrialStart.  # noqa: E501


        :return: The organization of this V1TrialStart.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this V1TrialStart.


        :param organization: The organization of this V1TrialStart.  # noqa: E501
        :type organization: str
        """

        self._organization = organization

    @property
    def plan(self):
        """Gets the plan of this V1TrialStart.  # noqa: E501


        :return: The plan of this V1TrialStart.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this V1TrialStart.


        :param plan: The plan of this V1TrialStart.  # noqa: E501
        :type plan: str
        """

        self._plan = plan

    @property
    def seats(self):
        """Gets the seats of this V1TrialStart.  # noqa: E501


        :return: The seats of this V1TrialStart.  # noqa: E501
        :rtype: int
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this V1TrialStart.


        :param seats: The seats of this V1TrialStart.  # noqa: E501
        :type seats: int
        """

        self._seats = seats

    @property
    def details(self):
        """Gets the details of this V1TrialStart.  # noqa: E501


        :return: The details of this V1TrialStart.  # noqa: E501
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this V1TrialStart.


        :param details: The details of this V1TrialStart.  # noqa: E501
        :type details: object
        """

        self._details = details

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
        if not isinstance(other, V1TrialStart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TrialStart):
            return True

        return self.to_dict() != other.to_dict()
