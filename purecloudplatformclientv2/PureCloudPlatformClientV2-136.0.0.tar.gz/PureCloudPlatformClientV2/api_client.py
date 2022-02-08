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

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import
from . import models
from .rest import RESTClientObject
from .rest import ApiException

import os
import re
import sys
import urllib
import json
import mimetypes
import random
import tempfile
import threading
import base64
import json
import time


from datetime import datetime
from datetime import date

# python 2 and python 3 compatibility library
from six import iteritems

try:
    # for python3
    from urllib.parse import quote
except ImportError:
    # for python2
    from urllib import quote

from .configuration import Configuration


class ApiClient(object):
    """
    Generic API client for Swagger client library builds.

    Swagger generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the Swagger
    templates.

    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.

    :param host: The base path for the server to call.
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to the API.
    """
    def __init__(self, host=None, header_name=None, header_value=None, cookie=None):

        """
        Constructor of the class.
        """
        self.rest_client = RESTClientObject()
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        if host is None:
            self.host = Configuration().host
        else:
            self.host = host
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'PureCloud SDK/python'

        # store clientId and clientSecret to request new access token for OAuth (Code Authorization)
        self.client_id = ""
        self.client_secret = ""
        # access token for OAuth
        self.access_token = ""
        # refresh token for OAuth (Code Authorization)
        self.refresh_token = ""
        # lock object used to ensure 1 thread tries to request a new access token
        self.refresh_token_lock = threading.Lock()
        # flag indicating a token refresh is being carried out
        self.refresh_in_progress = False



    def get_client_credentials_token(self, client_id, client_secret):
        """
        :param client_id: Client ID to authenticate with
        :param client_secret: Client Secret to Authenticate with
        :return: Returns the Api Object which allows this to directly enter into an api call, also sets the token
        """
        query_params = {}
        body = None
        url = re.sub(r'\/\/(api)\.', '//login.', self.host) + '/oauth/token'

        post_params = {'grant_type': 'client_credentials'}

        auth_string = 'Basic ' + base64.b64encode(bytes((client_id + ':' + client_secret).encode('ascii'))).decode(
            'ascii')

        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        header_params = self.sanitize_for_serialization(header_params)
        post_params = self.sanitize_for_serialization(post_params)

        response = self.request("POST", url,
                                query_params=query_params,
                                headers=header_params,
                                post_params=post_params, body=body);
        data = json.loads('[' + response.data + ']')
        self.access_token = data[0]["access_token"]
        return self;

    def get_saml2bearer_token(self,client_id,client_secret,org_name,assertion):
        """:param client_id: Client Id to authenticate with
         :param client_secret: Client Secret to authenticate with
         :param org_name: Orginization name to authenticate with
         :param assertion: SamlAssertion encoded
         :return:
         """

        query_params = {}
        body = None
        url = re.sub(r'\/\/(api)\.', '//login.', self.host) + '/oauth/token'

        post_params = {'grant_type': 'urn:ietf:params:oauth:grant-type:saml2-bearer',
                       'orgName': org_name,
                       'assertion': assertion
                       }

        auth_string = 'Basic ' + base64.b64encode(bytes((client_id + ':' + client_secret).encode('ascii'))).decode(
            'ascii')

        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        header_params = self.sanitize_for_serialization(header_params)
        post_params = self.sanitize_for_serialization(post_params)

        response = self.request("POST", url,
                                query_params=query_params,
                                headers=header_params,
                                post_params=post_params, body=body);
        data = json.loads('[' + response.data + ']')
        self.access_token = data[0]["access_token"]
        return self;  

    def get_code_authorization_token(self,client_id,client_secret,auth_code,redirect_uri):
        """:param client_id: Client Id to authenticate with
         :param client_secret: Client Secret to authenticate with
         :param auth_code: Authorization code
         :param redirect_uri: Authorized redirect URI for your Code Authorization client
         :return:
         """

        self.client_id = client_id
        self.client_secret = client_secret

        query_params = {}
        body = None
        url = re.sub(r'\/\/(api)\.', '//login.', self.host) + '/oauth/token'

        post_params = {'grant_type': 'authorization_code',
                       'code': auth_code,
                       'redirect_uri': redirect_uri
                       }

        auth_string = 'Basic ' + base64.b64encode(bytes((client_id + ':' + client_secret).encode('ascii'))).decode(
            'ascii')

        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        header_params = self.sanitize_for_serialization(header_params)
        post_params = self.sanitize_for_serialization(post_params)

        response = self.request("POST", url,
                                query_params=query_params,
                                headers=header_params,
                                post_params=post_params, body=body)
        data = json.loads('[' + response.data + ']')

        self.access_token = data[0]["access_token"]
        self.refresh_token = data[0]["refresh_token"]

        return self, data[0]

    def refresh_code_authorization_token(self,client_id,client_secret,refresh_token):
        """:param client_id: Client Id to authenticate with
         :param client_secret: Client Secret to authenticate with
         :param refresh_token: Refresh token used to request a new access token
         :return:
         """

        query_params = {}
        body = None
        url = re.sub(r'\/\/(api)\.', '//login.', self.host) + '/oauth/token'

        post_params = {'grant_type': 'refresh_token',
                       'refresh_token': refresh_token
                       }

        auth_string = 'Basic ' + base64.b64encode(bytes((client_id + ':' + client_secret).encode('ascii'))).decode(
            'ascii')

        header_params = {
            "Authorization": auth_string,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        header_params = self.sanitize_for_serialization(header_params)
        post_params = self.sanitize_for_serialization(post_params)

        response = self.request("POST", url,
                                query_params=query_params,
                                headers=header_params,
                                post_params=post_params, body=body)
        data = json.loads('[' + response.data + ']')

        self.access_token = data[0]["access_token"]
        self.refresh_token = data[0]["refresh_token"]

        return self, data[0]

    @property
    def user_agent(self):
        """
        Gets user agent.
        """
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        """
        Sets user agent.
        """
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def handle_expired_access_token(self):
        if self.refresh_token_lock.acquire(False):
            try:
                self.refresh_in_progress = True
                self.refresh_code_authorization_token(self.client_id, self.client_secret, self.refresh_token)
            finally:
                self.refresh_in_progress = False
                self.refresh_token_lock.release()
        else:
            start_time = time.time()
            sleep_duration = 0.200
            # Wait maximum of refresh_token_wait_time seconds for other thread to complete refresh
            # It would be ideal to use refresh_token_lock.acquire with a timeout value here but that was added in python 3.2 and we have to support older versions
            while time.time() - start_time < Configuration().refresh_token_wait_time:
                time.sleep(sleep_duration)
                if not self.refresh_in_progress:
                    return
            # Abort with error if we have waited refresh_token_wait_time seconds and refresh still isn't complete
            raise ApiException(
                status=500,
                reason="Token refresh took longer than `{0}` seconds"
                .format(str(Configuration().refresh_token_wait_time))
            )

    def __call_api(self, resource_path, method,
                   path_params=None, query_params=None, header_params=None,
                   body=None, post_params=None, files=None,
                   response_type=None, auth_settings=None, callback=None):
        # headers parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
        header_params['purecloud-sdk'] = '136.0.0'

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            for k, v in iteritems(path_params):
                replacement = quote(str(self.to_path_value(v)))
                resource_path = resource_path.\
                    replace('{' + k + '}', replacement)

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = {k: self.to_path_value(v)
                            for k, v in iteritems(query_params)}

        # post parameters
        if post_params or files:
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        url = self.host + resource_path

        response_data = None

        log_url = url
        if query_params:
            log_url += '?'
            i = 0
            for k, v in query_params.items():
                if i > 0:
                    log_url += '&'
                log_url += '{}={}'.format(k, v)
                i += 1

        try:
            # perform request and return response
            response_data = self.request(method, url, query_params=query_params,
                                        headers=header_params, post_params=post_params, body=body)
            Configuration().logger.trace(method, log_url, body, response_data.status, header_params, response_data.getheaders())
            Configuration().logger.debug(method, log_url, body, response_data.status, header_params)
        except ApiException as e:
            if Configuration().should_refresh_access_token and e.status == 401 and self.refresh_token != "":
                self.handle_expired_access_token()
                return self.__call_api(resource_path, method, path_params,
                            query_params, header_params, body, post_params,
                            files, response_type, auth_settings, callback)
            else:
                Configuration().logger.error(method, log_url, body, e.status, header_params, e.body, e.headers)
                raise

        self.last_response = response_data

        # deserialize response data
        if response_type:
            deserialized_data = self.deserialize(response_data, response_type)
        else:
            deserialized_data = None

        if callback:
            callback(deserialized_data)
        else:
            return deserialized_data

    def to_path_value(self, obj):
        """
        Takes value and turn it into a string suitable for inclusion in
        the path, by url-encoding.

        :param obj: object or string value.

        :return string: quoted value.
        """
        if type(obj) == list:
            return ','.join(obj)
        elif type(obj) == bool:
            return str(obj).lower()
        else:
            return str(obj)

    def sanitize_for_serialization(self, obj):
        """
        Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        types = (str, int, float, bool, tuple)
        if sys.version_info < (3,0):
            types = types + (unicode,)
        if isinstance(obj, type(None)):
            return None
        elif isinstance(obj, types):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            if isinstance(obj, dict):
                obj_dict = obj
            else:
                # Convert model obj to dict except
                # attributes `swagger_types`, `attribute_map`
                # and attributes which value is not None.
                # Convert attribute name to json key in
                # model definition for request.
                obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                            for attr, _ in iteritems(obj.swagger_types)
                            if getattr(obj, attr) is not None}

            return {key: self.sanitize_for_serialization(val)
                    for key, val in iteritems(obj_dict)}

    def deserialize(self, response, response_type):
        """
        Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialzied object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if "file" == response_type:
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """
        Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match('list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match('dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in iteritems(data)}

            # convert str to class
            # for native types
            if klass in ['int', 'float', 'str', 'bool',
                         "date", 'datetime', "object"]:
                klass = eval(klass)
            # for LocalDateTime special case, use datetime in Python
            elif klass == 'LocalDateTime':
                klass = eval('datetime')
            # for model types
            else:
                klass = eval('models.' + klass)

        if klass in [int, float, str, bool]:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == date:
            return self.__deserialize_date(data)
        elif klass == datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, callback=None):
        """
        Makes the HTTP request (synchronous) and return the deserialized data.
        To make an async request, define a function for callback.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param callback function: Callback function for asynchronous request.
            If provide this parameter,
            the request will be called asynchronously.
        :return:
            If provide parameter callback,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter callback is None,
            then the method will return the response directly.
        """
        if callback is None:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings, callback)
        else:
            thread = threading.Thread(target=self.__call_api,
                                      args=(resource_path, method,
                                            path_params, query_params,
                                            header_params, body,
                                            post_params, files,
                                            response_type, auth_settings,
                                            callback))
        thread.start()
        return thread

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None):
        """
        Makes the HTTP request using RESTClient.
        """
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           body=body)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def prepare_post_parameters(self, post_params=None, files=None):
        """
        Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if post_params:
            params = post_params

        if files:
            for k, v in iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = mimetypes.\
                            guess_type(filename)[0] or 'application/octet-stream'
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """
        Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = list(map(lambda x: x.lower(), accepts))

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """
        Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = list(map(lambda x: x.lower(), content_types))

        if 'application/json' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """
        Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters dict to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        config = Configuration()

        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = config.auth_settings(self.access_token).get(auth)
            if auth_setting:
                if not auth_setting['value']:
                    continue
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys[auth_setting['key']] = auth_setting['value']
                else:
                    raise ValueError(
                        'Authentication token must be in `query` or `header`'
                    )

    def __deserialize_file(self, response):
        """
        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        config = Configuration()

        fd, path = tempfile.mkstemp(dir=config.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.\
                search(r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition).\
                group(1)
            path = os.path.join(os.path.dirname(path), filename)

        with open(path, "w") as f:
            f.write(response.data)

        return path

    def __deserialize_primitive(self, data, klass):
        """
        Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, float, str, bool.
        """
        try:
            value = klass(data)
        except UnicodeEncodeError:
            value = unicode(data)
        except TypeError:
            value = data
        return value

    def __deserialize_object(self, value):
        """
        Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """
        Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import isoparse
            return isoparse(string).date()
        except ValueError:
            # Try parsing independent of ISO if we get a ValueError
            try:
                from dateutil.parser import parse
                return parse(string).date()
            except ImportError:
                return string
            # Not much we can do if `parse` returns a ValueError
            except ValueError:
                raise ApiException(
                    status=0,
                    reason="Failed to parse `{0}` into a date object"
                    .format(string)
                )
        except ImportError:
            return string

    def __deserialize_datatime(self, string):
        """
        Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import isoparse
            return isoparse(string)
        except ValueError:
            # Try parsing independent of ISO if we get a ValueError
            try:
                from dateutil.parser import parse
                return parse(string)
            except ImportError:
                return string
            # Not much we can do if `parse` returns a ValueError
            except ValueError:
                raise ApiException(
                    status=0,
                    reason="Failed to parse `{0}` into a datetime object".
                    format(string)
                )
        except ImportError:
            return string

    def __deserialize_model(self, data, klass):
        """
        Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """
        instance = klass()

        for attr, attr_type in iteritems(instance.swagger_types):
            if data is not None \
               and instance.attribute_map[attr] in data\
               and isinstance(data, (list, dict)):
                value = data[instance.attribute_map[attr]]
                setattr(instance, attr, self.__deserialize(value, attr_type))

        return instance
