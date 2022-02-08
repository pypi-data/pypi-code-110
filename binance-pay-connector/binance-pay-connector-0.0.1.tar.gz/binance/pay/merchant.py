from binance.pay.api import API
from binance.pay.lib.utils import check_required_parameters, check_required_parameter


class Merchant(API):
    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://bpay.binanceapi.com"
        super().__init__(key, secret, **kwargs)

    def new_order(self, params):
        """Create Order

        POST /binancepay/openapi/v2/order

        Create order API Version 2 used for merchant/partner to initiate acquiring order.
        https://developers.binance.com/docs/binance-pay/api-order-create-v2

        Args:
          merchant.subMerchantId (str, optional)
          env.terminalType (str)
          env.osType (str, optional)
          env.orderClientIp (str, optional)
          env.cookieId (str, optional)
          merchantTradeNo (str)
          orderAmount (float)
          currency (str)
          goods.goodsType (str)
          goods.goodsCategory (str)
          goods.referenceGoodsId (str)
          goods.goodsName (str)
          goods.goodsDetail (str)
          goods.goodsUnitAmount.currency (str)
          goods.goodsUnitAmount.amount (float)
          goods.goodsQuantity (str, optional)
          shipping.shippingName.firstName (str)
          shipping.shippingName.middleName (str, optional)
          shipping.shippingName.lastName (str)
          shipping.shippingAddress.region (str)
          shipping.shippingAddress.state (str, optional)
          shipping.shippingAddress.city (str, optional)
          shipping.shippingAddress.address (str, optional)
          shipping.shippingAddress.zipCode (str, optional)
          shipping.shippingAddress.shippingAddressType (str, optional)
          shipping.shippingAddress.shippingPhoneNo (str, optional)
          buyer.referenceBuyerId (str, optional)
          buyer.buyerName.firstName (str)
          buyer.buyerName.middleName (str, optional)
          buyer.buyerName.lastName (str)
          buyer.buyerPhoneCountryCode (str, optional)
          buyer.buyerPhoneNo (str, optional)
          buyer.buyerEmail (str, optional)
          buyer.buyerRegistrationTime (str, optional)
          buyer.buyerBrowserLanguage (str, optional)
          returnUrl (str, optional)
          cancelUrl (str, optional)
          orderExpireTime (int, optional)
          supportPayCurrency (str, optional)
          appId (str, optional)
        """
        return self.send_signed_request("POST", "/binancepay/openapi/v2/order", params)

    def get_order(self, **kwargs):
        """Query Order

        Query order API used for merchant/partner to query order status

        `POST /binancepay/openapi/v2/order/query`

        https://developers.binance.com/docs/binance-pay/api-order-query-v2

        Keyword Args:
          prepayId (str, optional) : Binance unique order id
          merchantTradeNo (str, optional) : The order id, Unique identifier for the request. Will be ignored if prepayId already provided
        """
        return self.send_signed_request(
            "POST", "/binancepay/openapi/v2/order/query", kwargs
        )

    def cancel_order(self, **kwargs):
        """Close Order

        Close order API used for merchant/partner to close order without any prior payment activities triggered by user. The successful close result will be notified asynchronously through Order Notification Webhook with bizStatus = "PAY_CLOSED"

        `POST /binancepay/openapi/order/close`

        https://developers.binance.com/docs/binance-pay/api-order-close

        Keyword Args:
          prepayId (str, optional) : Binance unique order id
          merchantTradeNo (str, optional) : The order id, Unique identifier for the request
        """

        return self.send_signed_request(
            "POST", "/binancepay/openapi/order/close", kwargs
        )

    def transfer_fund(
        self, requestId: str, currency: str, amount: str, transferType: str, **kwargs
    ):
        """Transfer Fund

        Fund transfer API used for merchant/partner to initiate Fund transfer between wallets.

        `POST /binancepay/openapi/wallet/transfer`

        https://developers.binance.com/docs/binance-pay/api-wallet-transfer

        Args:
          requestId (str) : Represents the unique ID of each transfer request.Generated by the merchant
          currency (str) : 	transfer currency, e.g. "BUSD"
          amount (str) : the transfer amount
          transferType (str) : Only `TO_MAIN` OR `TO_PAY`
        """

        check_required_parameters(
            [
                [requestId, "requestId"],
                [currency, "currency"],
                [amount, "amount"],
                [transferType, "transferType"],
            ]
        )

        payload = {
            "requestId": requestId,
            "currency": currency,
            "amount": amount,
            "transferType": transferType,
            **kwargs,
        }
        return self.send_signed_request(
            "POST", "/binancepay/openapi/wallet/transfer", payload
        )

    def get_transfer_result(self, tranId: str, **kwargs):
        """Query Transfer Result

        Query Transfer Result API used for merchant/partner to query transfer result.

        `POST /binancepay/openapi/wallet/transfer/query`

        https://developers.binance.com/docs/binance-pay/api-wallet-transfer-query

        Args:
          tranId (str) : the value of requestId of provoking Transfer Fund API
        """

        check_required_parameter(tranId, "tranId")

        payload = {"tranId": tranId, **kwargs}
        return self.send_signed_request(
            "POST", "/binancepay/openapi/wallet/transfer/query", payload
        )

    def new_sub_merchant(
        self,
        merchantName: str,
        merchantType: int,
        merchantMcc: str,
        country: str,
        **kwargs
    ):
        """Create SubMerchant

        Create Sub-merchant API used for merchant/partner.

        `POST /binancepay/openapi/submerchant/add`

        https://developers.binance.com/docs/binance-pay/api-submerchant-add

        Args:
          merchantName (str) : The sub merchant name maximum length 128, unique under one mainMerchantId.
          merchantType (int) :
            1=Personal(Individual) \n
            2=solo proprietor \n
            3=Partnership \n
            4=Private company \n
            5=Others company \n
          merchantMcc (str) : MCC Code, get from Binance
          country (str) : Country/Region of Business Operation,Can be multiple, split by "," eg:"SG,US" \n
            iso alpha 2 country code(https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), use "GO" if global
        Keyword Args:
          brandLogo (str, optional) : sub merchant logo url
          address (str, optional)
          companyName (str, optional)
          registrationNumber (str, optional)
          registrationCountry (str, optional)
          registrationAddress (str, optional)
          incorporationDate (int, optional)
          storeType (int, optional)
          siteType (int, optional)
          siteUrl (str, optional)
          siteName (str, optional)
          certificateType (int, optional) : 1=ID 2=Passport, Required if merchantType is Individual
          certificateCountry (str, optional)
          certificateNumber (str, optional)
          certificateValidDate (int, optional)
          contractTimeIsv (int, optional)
        """

        check_required_parameters(
            [
                [merchantName, "merchantName"],
                [merchantType, "merchantType"],
                [merchantMcc, "merchantMcc"],
                [country, "country"],
            ]
        )

        payload = {
            "merchantName": merchantName,
            "merchantType": merchantType,
            "merchantMcc": merchantMcc,
            "country": country,
            **kwargs,
        }

        return self.send_signed_request(
            "POST", "/binancepay/openapi/submerchant/add", payload
        )

    def refund_order(
        self, refundRequestId: str, prepayId: str, refundAmount: float, **kwargs
    ):
        """Refund Order

        Refund order API used for Marchant/Partner to refund for a successful payment.

        POST /binancepay/openapi/order/refund

        https://developers.binance.com/docs/binance-pay/api-order-refund

        Args:
          refundRequestId (str) : The unique ID assigned by the merchant to identify a refund request.The value must be same for one refund request.
          prepayId (str) : The unique ID assigned by Binance for the original order to be refunded.
          refundAmount (float) : You can perform multiple partial refunds, but their sum should not exceed the order amount.
        Keyword Args:
          refundReason (str, optional)
        """

        check_required_parameters(
            [
                [refundRequestId, "refundRequestId"],
                [prepayId, "prepayId"],
                [refundAmount, "refundAmount"],
            ]
        )

        payload = {
            "refundRequestId": refundRequestId,
            "prepayId": prepayId,
            "refundAmount": refundAmount,
            **kwargs,
        }
        return self.send_signed_request(
            "POST", "/binancepay/openapi/order/refund", payload
        )

    def get_refund_order(self, refundRequestId: str, **kwargs):
        """Query Refund Order

        Refund order API used for Marchant/Partner to refund for a successful payment.

        POST /binancepay/openapi/order/refund/query

        https://developers.binance.com/docs/binance-pay/api-order-refund

        Args:
          refundRequestId (str): The unique ID assigned by the merchant to identify a refund request.
        """

        check_required_parameter(refundRequestId, "refundRequestId")

        payload = {"refundRequestId": refundRequestId, **kwargs}
        return self.send_signed_request(
            "POST", "/binancepay/openapi/order/refund/query", payload
        )

    def batch_payout(
        self,
        requestId: str,
        batchName: str,
        currency: str,
        totalAmount: float,
        totalNumber: int,
        transferDetailList: dict,
        **kwargs
    ):
        """Batch Payout

        Payout API used for Merchant/Partner to make transfers in batch.

        POST /binancepay/openapi/payout/transfer

        https://developers.binance.com/docs/binance-pay/api-payout

        Args:
          requestId (str): The unique ID assigned by the merchant to identify a payout request.
          bizScene (str, optional)
          batchName (str) : The name of the batch payout.
          currency (str): Crypto token only, fiat NOT supported. All characters must be in uppercase
          totalAmount (float)
          totalNumber (int)
          transferDetailList.merchantSendId (str)
          transferDetailList.receiveType (str)
          transferDetailList.receiver (str)
          transferDetailList.transferAmount (float)
          transferDetailList.transferMethod (str) : FUNDING_WALLET, SPOT_WALLET
          transferDetailList.remark (str)
        Keyword Args:
          bizScene (str, optional)
        """

        check_required_parameters(
            [
                [requestId, "requestId"],
                [batchName, "batchName"],
                [currency, "currency"],
                [totalAmount, "totalAmount"],
                [totalNumber, "totalNumber"],
                [transferDetailList, "transferDetailList"],
            ]
        )

        payload = {
            "requestId": requestId,
            "batchName": batchName,
            "currency": currency,
            "totalAmount": totalAmount,
            "totalNumber": totalNumber,
            "transferDetailList": transferDetailList,
            **kwargs,
        }

        return self.send_signed_request(
            "POST", "/binancepay/openapi/payout/transfer", payload
        )

    def get_wallet_balance(self, wallet: str, currency: str, **kwargs):
        """Wallet Balance Query

        query wallet balance.

        POST /binancepay/openapi/balance

        https://developers.binance.com/docs/binance-pay/api-balance-query

        Args:
          wallet (str): FUNDING_WALLET, SPOT_WALLET
          currency (str): Currency to query, e.g, "BUSD"
        """

        check_required_parameters([[wallet, "wallet"], [currency, "currency"]])

        payload = {"wallet": wallet, "currency": currency, **kwargs}
        return self.send_signed_request("POST", "/binancepay/openapi/balance", payload)

    def get_payout(self, requestId: str, **kwargs):
        """Payout Query

        Payout query API used for Merchant/Partner to query transfer status.

        POST /binancepay/openapi/payout/query

        https://developers.binance.com/docs/binance-pay/api-payout-query

        Args:
          requestId (str): The unique ID assigned by the merchant to identify a payout request.
        Keyword Args:
          detailStatus (str)
        """

        check_required_parameter(requestId, "requestId")

        payload = {"requestId": requestId, **kwargs}
        return self.send_signed_request(
            "POST", "/binancepay/openapi/payout/query", payload
        )
