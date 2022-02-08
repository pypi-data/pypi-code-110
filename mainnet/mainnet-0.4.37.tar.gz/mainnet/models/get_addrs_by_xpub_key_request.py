# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.36
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class GetAddrsByXpubKeyRequest(object):
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
        'xpubkey': 'str',
        'path': 'str',
        'count': 'float'
    }

    attribute_map = {
        'xpubkey': 'xpubkey',
        'path': 'path',
        'count': 'count'
    }

    def __init__(self, xpubkey=None, path=None, count=None, local_vars_configuration=None):  # noqa: E501
        """GetAddrsByXpubKeyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._xpubkey = None
        self._path = None
        self._count = None
        self.discriminator = None

        if xpubkey is not None:
            self.xpubkey = xpubkey
        if path is not None:
            self.path = path
        if count is not None:
            self.count = count

    @property
    def xpubkey(self):
        """Gets the xpubkey of this GetAddrsByXpubKeyRequest.  # noqa: E501


        :return: The xpubkey of this GetAddrsByXpubKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._xpubkey

    @xpubkey.setter
    def xpubkey(self, xpubkey):
        """Sets the xpubkey of this GetAddrsByXpubKeyRequest.


        :param xpubkey: The xpubkey of this GetAddrsByXpubKeyRequest.  # noqa: E501
        :type xpubkey: str
        """

        self._xpubkey = xpubkey

    @property
    def path(self):
        """Gets the path of this GetAddrsByXpubKeyRequest.  # noqa: E501


        :return: The path of this GetAddrsByXpubKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this GetAddrsByXpubKeyRequest.


        :param path: The path of this GetAddrsByXpubKeyRequest.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def count(self):
        """Gets the count of this GetAddrsByXpubKeyRequest.  # noqa: E501


        :return: The count of this GetAddrsByXpubKeyRequest.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this GetAddrsByXpubKeyRequest.


        :param count: The count of this GetAddrsByXpubKeyRequest.  # noqa: E501
        :type count: float
        """

        self._count = count

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
        if not isinstance(other, GetAddrsByXpubKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAddrsByXpubKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
