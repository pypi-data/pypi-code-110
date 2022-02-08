#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.15.0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from polyaxon_sdk.configuration import Configuration


class V1SearchSpec(object):
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
        'query': 'str',
        'sort': 'str',
        'limit': 'int',
        'offset': 'int',
        'groupby': 'str',
        'columns': 'str',
        'layout': 'str',
        'sections': 'str',
        'compares': 'str',
        'heat': 'str',
        'events': 'V1DashboardSpec',
        'histograms': 'object',
        'trends': 'object',
        'analytics': 'V1AnalyticsSpec'
    }

    attribute_map = {
        'query': 'query',
        'sort': 'sort',
        'limit': 'limit',
        'offset': 'offset',
        'groupby': 'groupby',
        'columns': 'columns',
        'layout': 'layout',
        'sections': 'sections',
        'compares': 'compares',
        'heat': 'heat',
        'events': 'events',
        'histograms': 'histograms',
        'trends': 'trends',
        'analytics': 'analytics'
    }

    def __init__(self, query=None, sort=None, limit=None, offset=None, groupby=None, columns=None, layout=None, sections=None, compares=None, heat=None, events=None, histograms=None, trends=None, analytics=None, local_vars_configuration=None):  # noqa: E501
        """V1SearchSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._sort = None
        self._limit = None
        self._offset = None
        self._groupby = None
        self._columns = None
        self._layout = None
        self._sections = None
        self._compares = None
        self._heat = None
        self._events = None
        self._histograms = None
        self._trends = None
        self._analytics = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if sort is not None:
            self.sort = sort
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if groupby is not None:
            self.groupby = groupby
        if columns is not None:
            self.columns = columns
        if layout is not None:
            self.layout = layout
        if sections is not None:
            self.sections = sections
        if compares is not None:
            self.compares = compares
        if heat is not None:
            self.heat = heat
        if events is not None:
            self.events = events
        if histograms is not None:
            self.histograms = histograms
        if trends is not None:
            self.trends = trends
        if analytics is not None:
            self.analytics = analytics

    @property
    def query(self):
        """Gets the query of this V1SearchSpec.  # noqa: E501


        :return: The query of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this V1SearchSpec.


        :param query: The query of this V1SearchSpec.  # noqa: E501
        :type query: str
        """

        self._query = query

    @property
    def sort(self):
        """Gets the sort of this V1SearchSpec.  # noqa: E501


        :return: The sort of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this V1SearchSpec.


        :param sort: The sort of this V1SearchSpec.  # noqa: E501
        :type sort: str
        """

        self._sort = sort

    @property
    def limit(self):
        """Gets the limit of this V1SearchSpec.  # noqa: E501


        :return: The limit of this V1SearchSpec.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this V1SearchSpec.


        :param limit: The limit of this V1SearchSpec.  # noqa: E501
        :type limit: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this V1SearchSpec.  # noqa: E501


        :return: The offset of this V1SearchSpec.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this V1SearchSpec.


        :param offset: The offset of this V1SearchSpec.  # noqa: E501
        :type offset: int
        """

        self._offset = offset

    @property
    def groupby(self):
        """Gets the groupby of this V1SearchSpec.  # noqa: E501


        :return: The groupby of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._groupby

    @groupby.setter
    def groupby(self, groupby):
        """Sets the groupby of this V1SearchSpec.


        :param groupby: The groupby of this V1SearchSpec.  # noqa: E501
        :type groupby: str
        """

        self._groupby = groupby

    @property
    def columns(self):
        """Gets the columns of this V1SearchSpec.  # noqa: E501


        :return: The columns of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this V1SearchSpec.


        :param columns: The columns of this V1SearchSpec.  # noqa: E501
        :type columns: str
        """

        self._columns = columns

    @property
    def layout(self):
        """Gets the layout of this V1SearchSpec.  # noqa: E501


        :return: The layout of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this V1SearchSpec.


        :param layout: The layout of this V1SearchSpec.  # noqa: E501
        :type layout: str
        """

        self._layout = layout

    @property
    def sections(self):
        """Gets the sections of this V1SearchSpec.  # noqa: E501


        :return: The sections of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this V1SearchSpec.


        :param sections: The sections of this V1SearchSpec.  # noqa: E501
        :type sections: str
        """

        self._sections = sections

    @property
    def compares(self):
        """Gets the compares of this V1SearchSpec.  # noqa: E501


        :return: The compares of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._compares

    @compares.setter
    def compares(self, compares):
        """Sets the compares of this V1SearchSpec.


        :param compares: The compares of this V1SearchSpec.  # noqa: E501
        :type compares: str
        """

        self._compares = compares

    @property
    def heat(self):
        """Gets the heat of this V1SearchSpec.  # noqa: E501


        :return: The heat of this V1SearchSpec.  # noqa: E501
        :rtype: str
        """
        return self._heat

    @heat.setter
    def heat(self, heat):
        """Sets the heat of this V1SearchSpec.


        :param heat: The heat of this V1SearchSpec.  # noqa: E501
        :type heat: str
        """

        self._heat = heat

    @property
    def events(self):
        """Gets the events of this V1SearchSpec.  # noqa: E501


        :return: The events of this V1SearchSpec.  # noqa: E501
        :rtype: V1DashboardSpec
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this V1SearchSpec.


        :param events: The events of this V1SearchSpec.  # noqa: E501
        :type events: V1DashboardSpec
        """

        self._events = events

    @property
    def histograms(self):
        """Gets the histograms of this V1SearchSpec.  # noqa: E501


        :return: The histograms of this V1SearchSpec.  # noqa: E501
        :rtype: object
        """
        return self._histograms

    @histograms.setter
    def histograms(self, histograms):
        """Sets the histograms of this V1SearchSpec.


        :param histograms: The histograms of this V1SearchSpec.  # noqa: E501
        :type histograms: object
        """

        self._histograms = histograms

    @property
    def trends(self):
        """Gets the trends of this V1SearchSpec.  # noqa: E501


        :return: The trends of this V1SearchSpec.  # noqa: E501
        :rtype: object
        """
        return self._trends

    @trends.setter
    def trends(self, trends):
        """Sets the trends of this V1SearchSpec.


        :param trends: The trends of this V1SearchSpec.  # noqa: E501
        :type trends: object
        """

        self._trends = trends

    @property
    def analytics(self):
        """Gets the analytics of this V1SearchSpec.  # noqa: E501


        :return: The analytics of this V1SearchSpec.  # noqa: E501
        :rtype: V1AnalyticsSpec
        """
        return self._analytics

    @analytics.setter
    def analytics(self, analytics):
        """Sets the analytics of this V1SearchSpec.


        :param analytics: The analytics of this V1SearchSpec.  # noqa: E501
        :type analytics: V1AnalyticsSpec
        """

        self._analytics = analytics

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SearchSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SearchSpec):
            return True

        return self.to_dict() != other.to_dict()
