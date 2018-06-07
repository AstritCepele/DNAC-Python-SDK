# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NetworkDeviceBriefNIOResultResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'role': 'str',
        'role_source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'role': 'role',
        'role_source': 'roleSource'
    }

    def __init__(self, id=None, role=None, role_source=None):  # noqa: E501
        """NetworkDeviceBriefNIOResultResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._role = None
        self._role_source = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if role is not None:
            self.role = role
        if role_source is not None:
            self.role_source = role_source

    @property
    def id(self):
        """Gets the id of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501


        :return: The id of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkDeviceBriefNIOResultResponse.


        :param id: The id of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def role(self):
        """Gets the role of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501


        :return: The role of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NetworkDeviceBriefNIOResultResponse.


        :param role: The role of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def role_source(self):
        """Gets the role_source of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501


        :return: The role_source of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._role_source

    @role_source.setter
    def role_source(self, role_source):
        """Sets the role_source of this NetworkDeviceBriefNIOResultResponse.


        :param role_source: The role_source of this NetworkDeviceBriefNIOResultResponse.  # noqa: E501
        :type: str
        """

        self._role_source = role_source

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, NetworkDeviceBriefNIOResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
