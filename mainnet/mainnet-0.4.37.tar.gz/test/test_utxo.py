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
from mainnet.models.utxo import Utxo  # noqa: E501
from mainnet.rest import ApiException

class TestUtxo(unittest.TestCase):
    """Utxo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Utxo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.utxo.Utxo()  # noqa: E501
        if include_optional :
            return Utxo(
                index = 1.337, 
                tx_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f', 
                value = 100, 
                utxo_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f:0:21005'
            )
        else :
            return Utxo(
                tx_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f',
                value = 100,
                utxo_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f:0:21005',
        )

    def testUtxo(self):
        """Test Utxo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
