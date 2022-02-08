# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class SamplingCreateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'new_tag_name': 'TagName',
        'method': 'SamplingMethod',
        'config': 'SamplingConfig',
        'preselected_tag_id': 'MongoObjectID',
        'query_tag_id': 'MongoObjectID',
        'row_count': 'float'
    }

    attribute_map = {
        'new_tag_name': 'newTagName',
        'method': 'method',
        'config': 'config',
        'preselected_tag_id': 'preselectedTagId',
        'query_tag_id': 'queryTagId',
        'row_count': 'rowCount'
    }

    def __init__(self, new_tag_name=None, method=None, config=None, preselected_tag_id=None, query_tag_id=None, row_count=None, _configuration=None):  # noqa: E501
        """SamplingCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_tag_name = None
        self._method = None
        self._config = None
        self._preselected_tag_id = None
        self._query_tag_id = None
        self._row_count = None
        self.discriminator = None

        self.new_tag_name = new_tag_name
        self.method = method
        self.config = config
        if preselected_tag_id is not None:
            self.preselected_tag_id = preselected_tag_id
        if query_tag_id is not None:
            self.query_tag_id = query_tag_id
        if row_count is not None:
            self.row_count = row_count

    @property
    def new_tag_name(self):
        """Gets the new_tag_name of this SamplingCreateRequest.  # noqa: E501


        :return: The new_tag_name of this SamplingCreateRequest.  # noqa: E501
        :rtype: TagName
        """
        return self._new_tag_name

    @new_tag_name.setter
    def new_tag_name(self, new_tag_name):
        """Sets the new_tag_name of this SamplingCreateRequest.


        :param new_tag_name: The new_tag_name of this SamplingCreateRequest.  # noqa: E501
        :type: TagName
        """
        if self._configuration.client_side_validation and new_tag_name is None:
            raise ValueError("Invalid value for `new_tag_name`, must not be `None`")  # noqa: E501

        self._new_tag_name = new_tag_name

    @property
    def method(self):
        """Gets the method of this SamplingCreateRequest.  # noqa: E501


        :return: The method of this SamplingCreateRequest.  # noqa: E501
        :rtype: SamplingMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this SamplingCreateRequest.


        :param method: The method of this SamplingCreateRequest.  # noqa: E501
        :type: SamplingMethod
        """
        if self._configuration.client_side_validation and method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def config(self):
        """Gets the config of this SamplingCreateRequest.  # noqa: E501


        :return: The config of this SamplingCreateRequest.  # noqa: E501
        :rtype: SamplingConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this SamplingCreateRequest.


        :param config: The config of this SamplingCreateRequest.  # noqa: E501
        :type: SamplingConfig
        """
        if self._configuration.client_side_validation and config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def preselected_tag_id(self):
        """Gets the preselected_tag_id of this SamplingCreateRequest.  # noqa: E501


        :return: The preselected_tag_id of this SamplingCreateRequest.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._preselected_tag_id

    @preselected_tag_id.setter
    def preselected_tag_id(self, preselected_tag_id):
        """Sets the preselected_tag_id of this SamplingCreateRequest.


        :param preselected_tag_id: The preselected_tag_id of this SamplingCreateRequest.  # noqa: E501
        :type: MongoObjectID
        """

        self._preselected_tag_id = preselected_tag_id

    @property
    def query_tag_id(self):
        """Gets the query_tag_id of this SamplingCreateRequest.  # noqa: E501


        :return: The query_tag_id of this SamplingCreateRequest.  # noqa: E501
        :rtype: MongoObjectID
        """
        return self._query_tag_id

    @query_tag_id.setter
    def query_tag_id(self, query_tag_id):
        """Sets the query_tag_id of this SamplingCreateRequest.


        :param query_tag_id: The query_tag_id of this SamplingCreateRequest.  # noqa: E501
        :type: MongoObjectID
        """

        self._query_tag_id = query_tag_id

    @property
    def row_count(self):
        """Gets the row_count of this SamplingCreateRequest.  # noqa: E501

        temporary rowCount until the API/DB is aware how many they are..  # noqa: E501

        :return: The row_count of this SamplingCreateRequest.  # noqa: E501
        :rtype: float
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this SamplingCreateRequest.

        temporary rowCount until the API/DB is aware how many they are..  # noqa: E501

        :param row_count: The row_count of this SamplingCreateRequest.  # noqa: E501
        :type: float
        """

        self._row_count = row_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SamplingCreateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SamplingCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SamplingCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
