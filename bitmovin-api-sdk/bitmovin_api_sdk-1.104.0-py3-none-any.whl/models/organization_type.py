# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class OrganizationType(Enum):
    ROOT_ORGANIZATION = "ROOT_ORGANIZATION"
    SUB_ORGANIZATION = "SUB_ORGANIZATION"
