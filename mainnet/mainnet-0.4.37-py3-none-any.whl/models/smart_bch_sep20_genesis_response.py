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


class SmartBchSep20GenesisResponse(object):
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
        'token_id': 'str',
        'balance': 'SmartBchSep20BalanceResponse'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'balance': 'balance'
    }

    def __init__(self, token_id=None, balance=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchSep20GenesisResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token_id = None
        self._balance = None
        self.discriminator = None

        if token_id is not None:
            self.token_id = token_id
        if balance is not None:
            self.balance = balance

    @property
    def token_id(self):
        """Gets the token_id of this SmartBchSep20GenesisResponse.  # noqa: E501

        Full token identifier freshly created  # noqa: E501

        :return: The token_id of this SmartBchSep20GenesisResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SmartBchSep20GenesisResponse.

        Full token identifier freshly created  # noqa: E501

        :param token_id: The token_id of this SmartBchSep20GenesisResponse.  # noqa: E501
        :type token_id: str
        """

        self._token_id = token_id

    @property
    def balance(self):
        """Gets the balance of this SmartBchSep20GenesisResponse.  # noqa: E501


        :return: The balance of this SmartBchSep20GenesisResponse.  # noqa: E501
        :rtype: SmartBchSep20BalanceResponse
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SmartBchSep20GenesisResponse.


        :param balance: The balance of this SmartBchSep20GenesisResponse.  # noqa: E501
        :type balance: SmartBchSep20BalanceResponse
        """

        self._balance = balance

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
        if not isinstance(other, SmartBchSep20GenesisResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchSep20GenesisResponse):
            return True

        return self.to_dict() != other.to_dict()
