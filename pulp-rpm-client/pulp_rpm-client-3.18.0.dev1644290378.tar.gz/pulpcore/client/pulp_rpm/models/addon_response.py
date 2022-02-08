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

from pulpcore.client.pulp_rpm.configuration import Configuration


class AddonResponse(object):
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
        'addon_id': 'str',
        'uid': 'str',
        'name': 'str',
        'type': 'str',
        'packages': 'str'
    }

    attribute_map = {
        'addon_id': 'addon_id',
        'uid': 'uid',
        'name': 'name',
        'type': 'type',
        'packages': 'packages'
    }

    def __init__(self, addon_id=None, uid=None, name=None, type=None, packages=None, local_vars_configuration=None):  # noqa: E501
        """AddonResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addon_id = None
        self._uid = None
        self._name = None
        self._type = None
        self._packages = None
        self.discriminator = None

        self.addon_id = addon_id
        self.uid = uid
        self.name = name
        self.type = type
        self.packages = packages

    @property
    def addon_id(self):
        """Gets the addon_id of this AddonResponse.  # noqa: E501

        Addon id.  # noqa: E501

        :return: The addon_id of this AddonResponse.  # noqa: E501
        :rtype: str
        """
        return self._addon_id

    @addon_id.setter
    def addon_id(self, addon_id):
        """Sets the addon_id of this AddonResponse.

        Addon id.  # noqa: E501

        :param addon_id: The addon_id of this AddonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and addon_id is None:  # noqa: E501
            raise ValueError("Invalid value for `addon_id`, must not be `None`")  # noqa: E501

        self._addon_id = addon_id

    @property
    def uid(self):
        """Gets the uid of this AddonResponse.  # noqa: E501

        Addon uid.  # noqa: E501

        :return: The uid of this AddonResponse.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AddonResponse.

        Addon uid.  # noqa: E501

        :param uid: The uid of this AddonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def name(self):
        """Gets the name of this AddonResponse.  # noqa: E501

        Addon name.  # noqa: E501

        :return: The name of this AddonResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddonResponse.

        Addon name.  # noqa: E501

        :param name: The name of this AddonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this AddonResponse.  # noqa: E501

        Addon type.  # noqa: E501

        :return: The type of this AddonResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddonResponse.

        Addon type.  # noqa: E501

        :param type: The type of this AddonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def packages(self):
        """Gets the packages of this AddonResponse.  # noqa: E501

        Relative path to directory with binary RPMs.  # noqa: E501

        :return: The packages of this AddonResponse.  # noqa: E501
        :rtype: str
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this AddonResponse.

        Relative path to directory with binary RPMs.  # noqa: E501

        :param packages: The packages of this AddonResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and packages is None:  # noqa: E501
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

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
        if not isinstance(other, AddonResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddonResponse):
            return True

        return self.to_dict() != other.to_dict()
