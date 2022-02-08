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
import datetime

import mainnet
from mainnet.models.smart_bch_send_request_item_any_of import SmartBchSendRequestItemAnyOf  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchSendRequestItemAnyOf(unittest.TestCase):
    """SmartBchSendRequestItemAnyOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchSendRequestItemAnyOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_send_request_item_any_of.SmartBchSendRequestItemAnyOf()  # noqa: E501
        if include_optional :
            return SmartBchSendRequestItemAnyOf(
                address = '0xE25ddbAF8DD61b627727e03e190E32feddBD1319', 
                value = 100
            )
        else :
            return SmartBchSendRequestItemAnyOf(
                address = '0xE25ddbAF8DD61b627727e03e190E32feddBD1319',
                value = 100,
        )

    def testSmartBchSendRequestItemAnyOf(self):
        """Test SmartBchSendRequestItemAnyOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
