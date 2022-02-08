# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.36
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.smartbch_sep20_api import SmartbchSep20Api  # noqa: E501
from mainnet.rest import ApiException


class TestSmartbchSep20Api(unittest.TestCase):
    """SmartbchSep20Api unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.smartbch_sep20_api.SmartbchSep20Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_smart_bch_sep20_all_balances(self):
        """Test case for smart_bch_sep20_all_balances

        Get all SmartBch SEP20 balances of the wallet  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_balance(self):
        """Test case for smart_bch_sep20_balance

        Get total SmartBch SEP20 token balance of the wallet  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_deposit_address(self):
        """Test case for smart_bch_sep20_deposit_address

        Get an SmartBch SEP20 deposit address  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_deposit_qr(self):
        """Test case for smart_bch_sep20_deposit_qr

        Get an SmartBch SEP20 receiving address as a qrcode  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_genesis(self):
        """Test case for smart_bch_sep20_genesis

        Get created tokenId back and new SmartBch SEP20 token balance of the wallet  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_mint(self):
        """Test case for smart_bch_sep20_mint

        Get created tokenId back and new SmartBch SEP20 token balance of the wallet  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_send(self):
        """Test case for smart_bch_sep20_send

        Send some SmartBch SEP20 token amount to a given address  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_send_max(self):
        """Test case for smart_bch_sep20_send_max

        Send all available SmartBch SEP20 token funds to a given address  # noqa: E501
        """
        pass

    def test_smart_bch_sep20_token_info(self):
        """Test case for smart_bch_sep20_token_info

        Get information about the SmartBch SEP20 token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
