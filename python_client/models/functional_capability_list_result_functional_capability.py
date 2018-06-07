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

from python_client.models.functional_capability_list_result_function_details import FunctionalCapabilityListResultFunctionDetails  # noqa: F401,E501


class FunctionalCapabilityListResultFunctionalCapability(object):
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
        'attribute_info': 'object',
        'function_details': 'list[FunctionalCapabilityListResultFunctionDetails]',
        'function_name': 'str',
        'function_op_state': 'str',
        'id': 'str'
    }

    attribute_map = {
        'attribute_info': 'attributeInfo',
        'function_details': 'functionDetails',
        'function_name': 'functionName',
        'function_op_state': 'functionOpState',
        'id': 'id'
    }

    def __init__(self, attribute_info=None, function_details=None, function_name=None, function_op_state=None, id=None):  # noqa: E501
        """FunctionalCapabilityListResultFunctionalCapability - a model defined in Swagger"""  # noqa: E501

        self._attribute_info = None
        self._function_details = None
        self._function_name = None
        self._function_op_state = None
        self._id = None
        self.discriminator = None

        if attribute_info is not None:
            self.attribute_info = attribute_info
        if function_details is not None:
            self.function_details = function_details
        if function_name is not None:
            self.function_name = function_name
        if function_op_state is not None:
            self.function_op_state = function_op_state
        if id is not None:
            self.id = id

    @property
    def attribute_info(self):
        """Gets the attribute_info of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501


        :return: The attribute_info of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :rtype: object
        """
        return self._attribute_info

    @attribute_info.setter
    def attribute_info(self, attribute_info):
        """Sets the attribute_info of this FunctionalCapabilityListResultFunctionalCapability.


        :param attribute_info: The attribute_info of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :type: object
        """

        self._attribute_info = attribute_info

    @property
    def function_details(self):
        """Gets the function_details of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501


        :return: The function_details of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :rtype: list[FunctionalCapabilityListResultFunctionDetails]
        """
        return self._function_details

    @function_details.setter
    def function_details(self, function_details):
        """Sets the function_details of this FunctionalCapabilityListResultFunctionalCapability.


        :param function_details: The function_details of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :type: list[FunctionalCapabilityListResultFunctionDetails]
        """

        self._function_details = function_details

    @property
    def function_name(self):
        """Gets the function_name of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501


        :return: The function_name of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :rtype: str
        """
        return self._function_name

    @function_name.setter
    def function_name(self, function_name):
        """Sets the function_name of this FunctionalCapabilityListResultFunctionalCapability.


        :param function_name: The function_name of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :type: str
        """

        self._function_name = function_name

    @property
    def function_op_state(self):
        """Gets the function_op_state of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501


        :return: The function_op_state of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :rtype: str
        """
        return self._function_op_state

    @function_op_state.setter
    def function_op_state(self, function_op_state):
        """Sets the function_op_state of this FunctionalCapabilityListResultFunctionalCapability.


        :param function_op_state: The function_op_state of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "NOT_APPLICABLE", "DISABLED", "ENABLED"]  # noqa: E501
        if function_op_state not in allowed_values:
            raise ValueError(
                "Invalid value for `function_op_state` ({0}), must be one of {1}"  # noqa: E501
                .format(function_op_state, allowed_values)
            )

        self._function_op_state = function_op_state

    @property
    def id(self):
        """Gets the id of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501


        :return: The id of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FunctionalCapabilityListResultFunctionalCapability.


        :param id: The id of this FunctionalCapabilityListResultFunctionalCapability.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, FunctionalCapabilityListResultFunctionalCapability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
