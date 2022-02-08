# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmRepoMetadataFileResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'md5': 'str',
        'sha1': 'str',
        'sha224': 'str',
        'sha256': 'str',
        'sha384': 'str',
        'sha512': 'str',
        'artifact': 'str',
        'relative_path': 'str',
        'data_type': 'str',
        'checksum_type': 'str',
        'checksum': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'md5': 'md5',
        'sha1': 'sha1',
        'sha224': 'sha224',
        'sha256': 'sha256',
        'sha384': 'sha384',
        'sha512': 'sha512',
        'artifact': 'artifact',
        'relative_path': 'relative_path',
        'data_type': 'data_type',
        'checksum_type': 'checksum_type',
        'checksum': 'checksum'
    }

    def __init__(self, pulp_href=None, pulp_created=None, md5=None, sha1=None, sha224=None, sha256=None, sha384=None, sha512=None, artifact=None, relative_path=None, data_type=None, checksum_type=None, checksum=None, local_vars_configuration=None):  # noqa: E501
        """RpmRepoMetadataFileResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._md5 = None
        self._sha1 = None
        self._sha224 = None
        self._sha256 = None
        self._sha384 = None
        self._sha512 = None
        self._artifact = None
        self._relative_path = None
        self._data_type = None
        self._checksum_type = None
        self._checksum = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if md5 is not None:
            self.md5 = md5
        if sha1 is not None:
            self.sha1 = sha1
        if sha224 is not None:
            self.sha224 = sha224
        if sha256 is not None:
            self.sha256 = sha256
        if sha384 is not None:
            self.sha384 = sha384
        if sha512 is not None:
            self.sha512 = sha512
        if artifact is not None:
            self.artifact = artifact
        self.relative_path = relative_path
        self.data_type = data_type
        self.checksum_type = checksum_type
        self.checksum = checksum

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RpmRepoMetadataFileResponse.  # noqa: E501


        :return: The pulp_href of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RpmRepoMetadataFileResponse.


        :param pulp_href: The pulp_href of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RpmRepoMetadataFileResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RpmRepoMetadataFileResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def md5(self):
        """Gets the md5 of this RpmRepoMetadataFileResponse.  # noqa: E501

        The MD5 checksum if available.  # noqa: E501

        :return: The md5 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this RpmRepoMetadataFileResponse.

        The MD5 checksum if available.  # noqa: E501

        :param md5: The md5 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    @property
    def sha1(self):
        """Gets the sha1 of this RpmRepoMetadataFileResponse.  # noqa: E501

        The SHA-1 checksum if available.  # noqa: E501

        :return: The sha1 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this RpmRepoMetadataFileResponse.

        The SHA-1 checksum if available.  # noqa: E501

        :param sha1: The sha1 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._sha1 = sha1

    @property
    def sha224(self):
        """Gets the sha224 of this RpmRepoMetadataFileResponse.  # noqa: E501

        The SHA-224 checksum if available.  # noqa: E501

        :return: The sha224 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha224

    @sha224.setter
    def sha224(self, sha224):
        """Sets the sha224 of this RpmRepoMetadataFileResponse.

        The SHA-224 checksum if available.  # noqa: E501

        :param sha224: The sha224 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._sha224 = sha224

    @property
    def sha256(self):
        """Gets the sha256 of this RpmRepoMetadataFileResponse.  # noqa: E501

        The SHA-256 checksum if available.  # noqa: E501

        :return: The sha256 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this RpmRepoMetadataFileResponse.

        The SHA-256 checksum if available.  # noqa: E501

        :param sha256: The sha256 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._sha256 = sha256

    @property
    def sha384(self):
        """Gets the sha384 of this RpmRepoMetadataFileResponse.  # noqa: E501

        The SHA-384 checksum if available.  # noqa: E501

        :return: The sha384 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha384

    @sha384.setter
    def sha384(self, sha384):
        """Sets the sha384 of this RpmRepoMetadataFileResponse.

        The SHA-384 checksum if available.  # noqa: E501

        :param sha384: The sha384 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._sha384 = sha384

    @property
    def sha512(self):
        """Gets the sha512 of this RpmRepoMetadataFileResponse.  # noqa: E501

        The SHA-512 checksum if available.  # noqa: E501

        :return: The sha512 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._sha512

    @sha512.setter
    def sha512(self, sha512):
        """Sets the sha512 of this RpmRepoMetadataFileResponse.

        The SHA-512 checksum if available.  # noqa: E501

        :param sha512: The sha512 of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._sha512 = sha512

    @property
    def artifact(self):
        """Gets the artifact of this RpmRepoMetadataFileResponse.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this RpmRepoMetadataFileResponse.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this RpmRepoMetadataFileResponse.  # noqa: E501

        Relative path of the file.  # noqa: E501

        :return: The relative_path of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this RpmRepoMetadataFileResponse.

        Relative path of the file.  # noqa: E501

        :param relative_path: The relative_path of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relative_path is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def data_type(self):
        """Gets the data_type of this RpmRepoMetadataFileResponse.  # noqa: E501

        Metadata type.  # noqa: E501

        :return: The data_type of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this RpmRepoMetadataFileResponse.

        Metadata type.  # noqa: E501

        :param data_type: The data_type of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type

    @property
    def checksum_type(self):
        """Gets the checksum_type of this RpmRepoMetadataFileResponse.  # noqa: E501

        Checksum type for the file.  # noqa: E501

        :return: The checksum_type of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """Sets the checksum_type of this RpmRepoMetadataFileResponse.

        Checksum type for the file.  # noqa: E501

        :param checksum_type: The checksum_type of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and checksum_type is None:  # noqa: E501
            raise ValueError("Invalid value for `checksum_type`, must not be `None`")  # noqa: E501

        self._checksum_type = checksum_type

    @property
    def checksum(self):
        """Gets the checksum of this RpmRepoMetadataFileResponse.  # noqa: E501

        Checksum for the file.  # noqa: E501

        :return: The checksum of this RpmRepoMetadataFileResponse.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this RpmRepoMetadataFileResponse.

        Checksum for the file.  # noqa: E501

        :param checksum: The checksum of this RpmRepoMetadataFileResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and checksum is None:  # noqa: E501
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501

        self._checksum = checksum

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RpmRepoMetadataFileResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmRepoMetadataFileResponse):
            return True

        return self.to_dict() != other.to_dict()
