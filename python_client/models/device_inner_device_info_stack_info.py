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

from python_client.models.device_inner_device_info_stack_info_stack_member_list import DeviceInnerDeviceInfoStackInfoStackMemberList  # noqa: F401,E501


class DeviceInnerDeviceInfoStackInfo(object):
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
        'is_full_ring': 'bool',
        'stack_member_list': 'list[DeviceInnerDeviceInfoStackInfoStackMemberList]',
        'stack_ring_protocol': 'str',
        'supports_stack_workflows': 'bool',
        'total_member_count': 'int',
        'valid_license_levels': 'list[str]'
    }

    attribute_map = {
        'is_full_ring': 'isFullRing',
        'stack_member_list': 'stackMemberList',
        'stack_ring_protocol': 'stackRingProtocol',
        'supports_stack_workflows': 'supportsStackWorkflows',
        'total_member_count': 'totalMemberCount',
        'valid_license_levels': 'validLicenseLevels'
    }

    def __init__(self, is_full_ring=None, stack_member_list=None, stack_ring_protocol=None, supports_stack_workflows=None, total_member_count=None, valid_license_levels=None):  # noqa: E501
        """DeviceInnerDeviceInfoStackInfo - a model defined in Swagger"""  # noqa: E501

        self._is_full_ring = None
        self._stack_member_list = None
        self._stack_ring_protocol = None
        self._supports_stack_workflows = None
        self._total_member_count = None
        self._valid_license_levels = None
        self.discriminator = None

        if is_full_ring is not None:
            self.is_full_ring = is_full_ring
        if stack_member_list is not None:
            self.stack_member_list = stack_member_list
        if stack_ring_protocol is not None:
            self.stack_ring_protocol = stack_ring_protocol
        if supports_stack_workflows is not None:
            self.supports_stack_workflows = supports_stack_workflows
        if total_member_count is not None:
            self.total_member_count = total_member_count
        if valid_license_levels is not None:
            self.valid_license_levels = valid_license_levels

    @property
    def is_full_ring(self):
        """Gets the is_full_ring of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501


        :return: The is_full_ring of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_full_ring

    @is_full_ring.setter
    def is_full_ring(self, is_full_ring):
        """Sets the is_full_ring of this DeviceInnerDeviceInfoStackInfo.


        :param is_full_ring: The is_full_ring of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :type: bool
        """

        self._is_full_ring = is_full_ring

    @property
    def stack_member_list(self):
        """Gets the stack_member_list of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501


        :return: The stack_member_list of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :rtype: list[DeviceInnerDeviceInfoStackInfoStackMemberList]
        """
        return self._stack_member_list

    @stack_member_list.setter
    def stack_member_list(self, stack_member_list):
        """Sets the stack_member_list of this DeviceInnerDeviceInfoStackInfo.


        :param stack_member_list: The stack_member_list of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :type: list[DeviceInnerDeviceInfoStackInfoStackMemberList]
        """

        self._stack_member_list = stack_member_list

    @property
    def stack_ring_protocol(self):
        """Gets the stack_ring_protocol of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501


        :return: The stack_ring_protocol of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :rtype: str
        """
        return self._stack_ring_protocol

    @stack_ring_protocol.setter
    def stack_ring_protocol(self, stack_ring_protocol):
        """Sets the stack_ring_protocol of this DeviceInnerDeviceInfoStackInfo.


        :param stack_ring_protocol: The stack_ring_protocol of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :type: str
        """

        self._stack_ring_protocol = stack_ring_protocol

    @property
    def supports_stack_workflows(self):
        """Gets the supports_stack_workflows of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501


        :return: The supports_stack_workflows of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :rtype: bool
        """
        return self._supports_stack_workflows

    @supports_stack_workflows.setter
    def supports_stack_workflows(self, supports_stack_workflows):
        """Sets the supports_stack_workflows of this DeviceInnerDeviceInfoStackInfo.


        :param supports_stack_workflows: The supports_stack_workflows of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :type: bool
        """

        self._supports_stack_workflows = supports_stack_workflows

    @property
    def total_member_count(self):
        """Gets the total_member_count of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501


        :return: The total_member_count of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_member_count

    @total_member_count.setter
    def total_member_count(self, total_member_count):
        """Sets the total_member_count of this DeviceInnerDeviceInfoStackInfo.


        :param total_member_count: The total_member_count of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :type: int
        """

        self._total_member_count = total_member_count

    @property
    def valid_license_levels(self):
        """Gets the valid_license_levels of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501


        :return: The valid_license_levels of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_license_levels

    @valid_license_levels.setter
    def valid_license_levels(self, valid_license_levels):
        """Sets the valid_license_levels of this DeviceInnerDeviceInfoStackInfo.


        :param valid_license_levels: The valid_license_levels of this DeviceInnerDeviceInfoStackInfo.  # noqa: E501
        :type: list[str]
        """

        self._valid_license_levels = valid_license_levels

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
        if not isinstance(other, DeviceInnerDeviceInfoStackInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other