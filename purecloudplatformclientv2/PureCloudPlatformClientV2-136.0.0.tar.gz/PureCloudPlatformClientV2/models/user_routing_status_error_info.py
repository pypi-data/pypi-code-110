# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class UserRoutingStatusErrorInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserRoutingStatusErrorInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_code': 'str',
            'status': 'int',
            'correlation_id': 'str',
            'user_message': 'str',
            'user_params_message': 'str',
            'user_params': 'list[UserRoutingStatusUserParam]'
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'status': 'status',
            'correlation_id': 'correlationId',
            'user_message': 'userMessage',
            'user_params_message': 'userParamsMessage',
            'user_params': 'userParams'
        }

        self._error_code = None
        self._status = None
        self._correlation_id = None
        self._user_message = None
        self._user_params_message = None
        self._user_params = None

    @property
    def error_code(self):
        """
        Gets the error_code of this UserRoutingStatusErrorInfo.
        A code unique to this error. Typically prefixed with the service that originated the error. For example CONFIG_USER_NOT_FOUND

        :return: The error_code of this UserRoutingStatusErrorInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this UserRoutingStatusErrorInfo.
        A code unique to this error. Typically prefixed with the service that originated the error. For example CONFIG_USER_NOT_FOUND

        :param error_code: The error_code of this UserRoutingStatusErrorInfo.
        :type: str
        """
        
        self._error_code = error_code

    @property
    def status(self):
        """
        Gets the status of this UserRoutingStatusErrorInfo.
        The HTTP status code for this message. If left blank the status code from the HTTP response is used.

        :return: The status of this UserRoutingStatusErrorInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserRoutingStatusErrorInfo.
        The HTTP status code for this message. If left blank the status code from the HTTP response is used.

        :param status: The status of this UserRoutingStatusErrorInfo.
        :type: int
        """
        
        self._status = status

    @property
    def correlation_id(self):
        """
        Gets the correlation_id of this UserRoutingStatusErrorInfo.
        The correlation Id or context Id for this message. If left blank the Public API will look at the HTTP response header 'ININ-Correlation-Id' instead.

        :return: The correlation_id of this UserRoutingStatusErrorInfo.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """
        Sets the correlation_id of this UserRoutingStatusErrorInfo.
        The correlation Id or context Id for this message. If left blank the Public API will look at the HTTP response header 'ININ-Correlation-Id' instead.

        :param correlation_id: The correlation_id of this UserRoutingStatusErrorInfo.
        :type: str
        """
        
        self._correlation_id = correlation_id

    @property
    def user_message(self):
        """
        Gets the user_message of this UserRoutingStatusErrorInfo.
        A customer friendly message. This should be a complete sentence, use proper grammar and only include information useful to a customer. This is not a dev message and should not include things like Org Id

        :return: The user_message of this UserRoutingStatusErrorInfo.
        :rtype: str
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message):
        """
        Sets the user_message of this UserRoutingStatusErrorInfo.
        A customer friendly message. This should be a complete sentence, use proper grammar and only include information useful to a customer. This is not a dev message and should not include things like Org Id

        :param user_message: The user_message of this UserRoutingStatusErrorInfo.
        :type: str
        """
        
        self._user_message = user_message

    @property
    def user_params_message(self):
        """
        Gets the user_params_message of this UserRoutingStatusErrorInfo.
        This is the same as userMessage except it uses template fields for variable replacement. For instance: 'User {username} was not found'

        :return: The user_params_message of this UserRoutingStatusErrorInfo.
        :rtype: str
        """
        return self._user_params_message

    @user_params_message.setter
    def user_params_message(self, user_params_message):
        """
        Sets the user_params_message of this UserRoutingStatusErrorInfo.
        This is the same as userMessage except it uses template fields for variable replacement. For instance: 'User {username} was not found'

        :param user_params_message: The user_params_message of this UserRoutingStatusErrorInfo.
        :type: str
        """
        
        self._user_params_message = user_params_message

    @property
    def user_params(self):
        """
        Gets the user_params of this UserRoutingStatusErrorInfo.
        Used in conjunction with userParamsMessage. These are the template parameters. For instance: UserParam.key = 'username', UserParam.value = 'chuck.pulfer'

        :return: The user_params of this UserRoutingStatusErrorInfo.
        :rtype: list[UserRoutingStatusUserParam]
        """
        return self._user_params

    @user_params.setter
    def user_params(self, user_params):
        """
        Sets the user_params of this UserRoutingStatusErrorInfo.
        Used in conjunction with userParamsMessage. These are the template parameters. For instance: UserParam.key = 'username', UserParam.value = 'chuck.pulfer'

        :param user_params: The user_params of this UserRoutingStatusErrorInfo.
        :type: list[UserRoutingStatusUserParam]
        """
        
        self._user_params = user_params

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

