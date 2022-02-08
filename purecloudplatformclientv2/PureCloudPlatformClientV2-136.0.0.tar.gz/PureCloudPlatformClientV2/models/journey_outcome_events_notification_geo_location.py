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

class JourneyOutcomeEventsNotificationGeoLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JourneyOutcomeEventsNotificationGeoLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country': 'str',
            'country_name': 'str',
            'latitude': 'float',
            'longitude': 'float',
            'locality': 'str',
            'postal_code': 'str',
            'region': 'str',
            'region_name': 'str',
            'timezone': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'country': 'country',
            'country_name': 'countryName',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'locality': 'locality',
            'postal_code': 'postalCode',
            'region': 'region',
            'region_name': 'regionName',
            'timezone': 'timezone',
            'source': 'source'
        }

        self._country = None
        self._country_name = None
        self._latitude = None
        self._longitude = None
        self._locality = None
        self._postal_code = None
        self._region = None
        self._region_name = None
        self._timezone = None
        self._source = None

    @property
    def country(self):
        """
        Gets the country of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The country of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this JourneyOutcomeEventsNotificationGeoLocation.


        :param country: The country of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._country = country

    @property
    def country_name(self):
        """
        Gets the country_name of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The country_name of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this JourneyOutcomeEventsNotificationGeoLocation.


        :param country_name: The country_name of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._country_name = country_name

    @property
    def latitude(self):
        """
        Gets the latitude of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The latitude of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this JourneyOutcomeEventsNotificationGeoLocation.


        :param latitude: The latitude of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: float
        """
        
        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The longitude of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this JourneyOutcomeEventsNotificationGeoLocation.


        :param longitude: The longitude of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: float
        """
        
        self._longitude = longitude

    @property
    def locality(self):
        """
        Gets the locality of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The locality of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this JourneyOutcomeEventsNotificationGeoLocation.


        :param locality: The locality of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._locality = locality

    @property
    def postal_code(self):
        """
        Gets the postal_code of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The postal_code of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this JourneyOutcomeEventsNotificationGeoLocation.


        :param postal_code: The postal_code of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._postal_code = postal_code

    @property
    def region(self):
        """
        Gets the region of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The region of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this JourneyOutcomeEventsNotificationGeoLocation.


        :param region: The region of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._region = region

    @property
    def region_name(self):
        """
        Gets the region_name of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The region_name of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """
        Sets the region_name of this JourneyOutcomeEventsNotificationGeoLocation.


        :param region_name: The region_name of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._region_name = region_name

    @property
    def timezone(self):
        """
        Gets the timezone of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The timezone of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this JourneyOutcomeEventsNotificationGeoLocation.


        :param timezone: The timezone of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._timezone = timezone

    @property
    def source(self):
        """
        Gets the source of this JourneyOutcomeEventsNotificationGeoLocation.


        :return: The source of this JourneyOutcomeEventsNotificationGeoLocation.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this JourneyOutcomeEventsNotificationGeoLocation.


        :param source: The source of this JourneyOutcomeEventsNotificationGeoLocation.
        :type: str
        """
        
        self._source = source

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

