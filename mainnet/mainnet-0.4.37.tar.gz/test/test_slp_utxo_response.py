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
from mainnet.models.slp_utxo_response import SlpUtxoResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSlpUtxoResponse(unittest.TestCase):
    """SlpUtxoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SlpUtxoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.slp_utxo_response.SlpUtxoResponse()  # noqa: E501
        if include_optional :
            return SlpUtxoResponse(
                utxos = [
                    mainnet.models.slp_utxo.SlpUtxo(
                        index = 1.337, 
                        tx_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f', 
                        satoshis = 546, 
                        utxo_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f:0', 
                        value = '10000', 
                        decimals = 2, 
                        ticker = 'MNC', 
                        token_id = '132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15', 
                        type = 1, )
                    ]
            )
        else :
            return SlpUtxoResponse(
        )

    def testSlpUtxoResponse(self):
        """Test SlpUtxoResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
