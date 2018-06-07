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

from python_client.models.reset_request_config_list import ResetRequestConfigList  # noqa: F401,E501


class DeviceInnerWorkflowParameters(object):
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
        'config_list': 'list[ResetRequestConfigList]',
        'license_level': 'str',
        'license_type': 'str',
        'top_of_stack_serial_number': 'str'
    }

    attribute_map = {
        'config_list': 'configList',
        'license_level': 'licenseLevel',
        'license_type': 'licenseType',
        'top_of_stack_serial_number': 'topOfStackSerialNumber'
    }

    def __init__(self, config_list=None, license_level=None, license_type=None, top_of_stack_serial_number=None):  # noqa: E501
        """DeviceInnerWorkflowParameters - a model defined in Swagger"""  # noqa: E501

        self._config_list = None
        self._license_level = None
        self._license_type = None
        self._top_of_stack_serial_number = None
        self.discriminator = None

        if config_list is not None:
            self.config_list = config_list
        if license_level is not None:
            self.license_level = license_level
        if license_type is not None:
            self.license_type = license_type
        if top_of_stack_serial_number is not None:
            self.top_of_stack_serial_number = top_of_stack_serial_number

    @property
    def config_list(self):
        """Gets the config_list of this DeviceInnerWorkflowParameters.  # noqa: E501


        :return: The config_list of this DeviceInnerWorkflowParameters.  # noqa: E501
        :rtype: list[ResetRequestConfigList]
        """
        return self._config_list

    @config_list.setter
    def config_list(self, config_list):
        """Sets the config_list of this DeviceInnerWorkflowParameters.


        :param config_list: The config_list of this DeviceInnerWorkflowParameters.  # noqa: E501
        :type: list[ResetRequestConfigList]
        """

        self._config_list = config_list

    @property
    def license_level(self):
        """Gets the license_level of this DeviceInnerWorkflowParameters.  # noqa: E501


        :return: The license_level of this DeviceInnerWorkflowParameters.  # noqa: E501
        :rtype: str
        """
        return self._license_level

    @license_level.setter
    def license_level(self, license_level):
        """Sets the license_level of this DeviceInnerWorkflowParameters.


        :param license_level: The license_level of this DeviceInnerWorkflowParameters.  # noqa: E501
        :type: str
        """

        self._license_level = license_level

    @property
    def license_type(self):
        """Gets the license_type of this DeviceInnerWorkflowParameters.  # noqa: E501


        :return: The license_type of this DeviceInnerWorkflowParameters.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this DeviceInnerWorkflowParameters.


        :param license_type: The license_type of this DeviceInnerWorkflowParameters.  # noqa: E501
        :type: str
        """

        self._license_type = license_type

    @property
    def top_of_stack_serial_number(self):
        """Gets the top_of_stack_serial_number of this DeviceInnerWorkflowParameters.  # noqa: E501


        :return: The top_of_stack_serial_number of this DeviceInnerWorkflowParameters.  # noqa: E501
        :rtype: str
        """
        return self._top_of_stack_serial_number

    @top_of_stack_serial_number.setter
    def top_of_stack_serial_number(self, top_of_stack_serial_number):
        """Sets the top_of_stack_serial_number of this DeviceInnerWorkflowParameters.


        :param top_of_stack_serial_number: The top_of_stack_serial_number of this DeviceInnerWorkflowParameters.  # noqa: E501
        :type: str
        """

        self._top_of_stack_serial_number = top_of_stack_serial_number

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
        if not isinstance(other, DeviceInnerWorkflowParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
