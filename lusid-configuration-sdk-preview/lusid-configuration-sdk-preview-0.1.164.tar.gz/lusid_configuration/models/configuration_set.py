# coding: utf-8

"""
    FINBOURNE ConfigurationService API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.164
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_configuration.configuration import Configuration


class ConfigurationSet(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'created_at': 'datetime',
        'created_by': 'str',
        'last_modified_at': 'datetime',
        'last_modified_by': 'str',
        'description': 'str',
        'items': 'list[ConfigurationItemSummary]',
        'id': 'ResourceId',
        'type': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'last_modified_at': 'lastModifiedAt',
        'last_modified_by': 'lastModifiedBy',
        'description': 'description',
        'items': 'items',
        'id': 'id',
        'type': 'type'
    }

    required_map = {
        'created_at': 'required',
        'created_by': 'required',
        'last_modified_at': 'required',
        'last_modified_by': 'required',
        'description': 'optional',
        'items': 'optional',
        'id': 'required',
        'type': 'required'
    }

    def __init__(self, created_at=None, created_by=None, last_modified_at=None, last_modified_by=None, description=None, items=None, id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ConfigurationSet - a model defined in OpenAPI"
        
        :param created_at:  The date referring to the creation date of the configuration set (required)
        :type created_at: datetime
        :param created_by:  Who created the configuration set (required)
        :type created_by: str
        :param last_modified_at:  The date referring to the date when the configuration set was last modified (required)
        :type last_modified_at: datetime
        :param last_modified_by:  Who modified the configuration set most recently (required)
        :type last_modified_by: str
        :param description:  Describes the configuration set
        :type description: str
        :param items:  The collection of the configuration items that this set contains.
        :type items: list[lusid_configuration.ConfigurationItemSummary]
        :param id:  (required)
        :type id: lusid_configuration.ResourceId
        :param type:  The type (personal or shared) of the configuration set (required)
        :type type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._created_by = None
        self._last_modified_at = None
        self._last_modified_by = None
        self._description = None
        self._items = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.created_at = created_at
        self.created_by = created_by
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.description = description
        self.items = items
        self.id = id
        self.type = type

    @property
    def created_at(self):
        """Gets the created_at of this ConfigurationSet.  # noqa: E501

        The date referring to the creation date of the configuration set  # noqa: E501

        :return: The created_at of this ConfigurationSet.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConfigurationSet.

        The date referring to the creation date of the configuration set  # noqa: E501

        :param created_at: The created_at of this ConfigurationSet.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this ConfigurationSet.  # noqa: E501

        Who created the configuration set  # noqa: E501

        :return: The created_by of this ConfigurationSet.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ConfigurationSet.

        Who created the configuration set  # noqa: E501

        :param created_by: The created_by of this ConfigurationSet.  # noqa: E501
        :type created_by: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this ConfigurationSet.  # noqa: E501

        The date referring to the date when the configuration set was last modified  # noqa: E501

        :return: The last_modified_at of this ConfigurationSet.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this ConfigurationSet.

        The date referring to the date when the configuration set was last modified  # noqa: E501

        :param last_modified_at: The last_modified_at of this ConfigurationSet.  # noqa: E501
        :type last_modified_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ConfigurationSet.  # noqa: E501

        Who modified the configuration set most recently  # noqa: E501

        :return: The last_modified_by of this ConfigurationSet.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ConfigurationSet.

        Who modified the configuration set most recently  # noqa: E501

        :param last_modified_by: The last_modified_by of this ConfigurationSet.  # noqa: E501
        :type last_modified_by: str
        """
        if self.local_vars_configuration.client_side_validation and last_modified_by is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_by`, must not be `None`")  # noqa: E501

        self._last_modified_by = last_modified_by

    @property
    def description(self):
        """Gets the description of this ConfigurationSet.  # noqa: E501

        Describes the configuration set  # noqa: E501

        :return: The description of this ConfigurationSet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationSet.

        Describes the configuration set  # noqa: E501

        :param description: The description of this ConfigurationSet.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def items(self):
        """Gets the items of this ConfigurationSet.  # noqa: E501

        The collection of the configuration items that this set contains.  # noqa: E501

        :return: The items of this ConfigurationSet.  # noqa: E501
        :rtype: list[lusid_configuration.ConfigurationItemSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ConfigurationSet.

        The collection of the configuration items that this set contains.  # noqa: E501

        :param items: The items of this ConfigurationSet.  # noqa: E501
        :type items: list[lusid_configuration.ConfigurationItemSummary]
        """

        self._items = items

    @property
    def id(self):
        """Gets the id of this ConfigurationSet.  # noqa: E501


        :return: The id of this ConfigurationSet.  # noqa: E501
        :rtype: lusid_configuration.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigurationSet.


        :param id: The id of this ConfigurationSet.  # noqa: E501
        :type id: lusid_configuration.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this ConfigurationSet.  # noqa: E501

        The type (personal or shared) of the configuration set  # noqa: E501

        :return: The type of this ConfigurationSet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigurationSet.

        The type (personal or shared) of the configuration set  # noqa: E501

        :param type: The type of this ConfigurationSet.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, ConfigurationSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigurationSet):
            return True

        return self.to_dict() != other.to_dict()
