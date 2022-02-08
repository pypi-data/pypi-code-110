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
from mainnet.api.util_api import UtilApi  # noqa: E501
from mainnet.rest import ApiException


class TestUtilApi(unittest.TestCase):
    """UtilApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.util_api.UtilApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_convert(self):
        """Test case for convert

        convert between units  # noqa: E501
        """
        pass

    def test_get_addrs_by_xpub_key(self):
        """Test case for get_addrs_by_xpub_key

        Derive heristic determined addresses from an extended public key, per BIP32  # noqa: E501
        """
        pass

    def test_get_xpub_key_info(self):
        """Test case for get_xpub_key_info

        Decode information about an extended public key, per BIP32  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
