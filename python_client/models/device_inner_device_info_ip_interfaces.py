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


class DeviceInnerDeviceInfoIpInterfaces(object):
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
        'ipv4_address': 'object',
        'ipv6_address_list': 'list[object]',
        'mac_address': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'ipv4_address': 'ipv4Address',
        'ipv6_address_list': 'ipv6AddressList',
        'mac_address': 'macAddress',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, ipv4_address=None, ipv6_address_list=None, mac_address=None, name=None, status=None):  # noqa: E501
        """DeviceInnerDeviceInfoIpInterfaces - a model defined in Swagger"""  # noqa: E501

        self._ipv4_address = None
        self._ipv6_address_list = None
        self._mac_address = None
        self._name = None
        self._status = None
        self.discriminator = None

        if ipv4_address is not None:
            self.ipv4_address = ipv4_address
        if ipv6_address_list is not None:
            self.ipv6_address_list = ipv6_address_list
        if mac_address is not None:
            self.mac_address = mac_address
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501


        :return: The ipv4_address of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :rtype: object
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this DeviceInnerDeviceInfoIpInterfaces.


        :param ipv4_address: The ipv4_address of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :type: object
        """

        self._ipv4_address = ipv4_address

    @property
    def ipv6_address_list(self):
        """Gets the ipv6_address_list of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501


        :return: The ipv6_address_list of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :rtype: list[object]
        """
        return self._ipv6_address_list

    @ipv6_address_list.setter
    def ipv6_address_list(self, ipv6_address_list):
        """Sets the ipv6_address_list of this DeviceInnerDeviceInfoIpInterfaces.


        :param ipv6_address_list: The ipv6_address_list of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :type: list[object]
        """

        self._ipv6_address_list = ipv6_address_list

    @property
    def mac_address(self):
        """Gets the mac_address of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501


        :return: The mac_address of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this DeviceInnerDeviceInfoIpInterfaces.


        :param mac_address: The mac_address of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501


        :return: The name of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceInnerDeviceInfoIpInterfaces.


        :param name: The name of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501


        :return: The status of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeviceInnerDeviceInfoIpInterfaces.


        :param status: The status of this DeviceInnerDeviceInfoIpInterfaces.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, DeviceInnerDeviceInfoIpInterfaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
