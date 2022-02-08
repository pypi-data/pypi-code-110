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


class ElectrumRawTransactionScriptPubKey(object):
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
        'addresses': 'list[str]',
        'asm': 'str',
        'hex': 'str',
        'req_sigs': 'float',
        'type': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'asm': 'asm',
        'hex': 'hex',
        'req_sigs': 'reqSigs',
        'type': 'type'
    }

    def __init__(self, addresses=None, asm=None, hex=None, req_sigs=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ElectrumRawTransactionScriptPubKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._asm = None
        self._hex = None
        self._req_sigs = None
        self._type = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if asm is not None:
            self.asm = asm
        if hex is not None:
            self.hex = hex
        if req_sigs is not None:
            self.req_sigs = req_sigs
        if type is not None:
            self.type = type

    @property
    def addresses(self):
        """Gets the addresses of this ElectrumRawTransactionScriptPubKey.  # noqa: E501


        :return: The addresses of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ElectrumRawTransactionScriptPubKey.


        :param addresses: The addresses of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :type addresses: list[str]
        """

        self._addresses = addresses

    @property
    def asm(self):
        """Gets the asm of this ElectrumRawTransactionScriptPubKey.  # noqa: E501


        :return: The asm of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :rtype: str
        """
        return self._asm

    @asm.setter
    def asm(self, asm):
        """Sets the asm of this ElectrumRawTransactionScriptPubKey.


        :param asm: The asm of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :type asm: str
        """

        self._asm = asm

    @property
    def hex(self):
        """Gets the hex of this ElectrumRawTransactionScriptPubKey.  # noqa: E501


        :return: The hex of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Sets the hex of this ElectrumRawTransactionScriptPubKey.


        :param hex: The hex of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :type hex: str
        """

        self._hex = hex

    @property
    def req_sigs(self):
        """Gets the req_sigs of this ElectrumRawTransactionScriptPubKey.  # noqa: E501


        :return: The req_sigs of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :rtype: float
        """
        return self._req_sigs

    @req_sigs.setter
    def req_sigs(self, req_sigs):
        """Sets the req_sigs of this ElectrumRawTransactionScriptPubKey.


        :param req_sigs: The req_sigs of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :type req_sigs: float
        """

        self._req_sigs = req_sigs

    @property
    def type(self):
        """Gets the type of this ElectrumRawTransactionScriptPubKey.  # noqa: E501


        :return: The type of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElectrumRawTransactionScriptPubKey.


        :param type: The type of this ElectrumRawTransactionScriptPubKey.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, ElectrumRawTransactionScriptPubKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectrumRawTransactionScriptPubKey):
            return True

        return self.to_dict() != other.to_dict()
