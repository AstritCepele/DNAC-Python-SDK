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


class TemplateDTODeviceTypes(object):
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
        'product_family': 'str',
        'product_series': 'str',
        'product_type': 'str'
    }

    attribute_map = {
        'product_family': 'productFamily',
        'product_series': 'productSeries',
        'product_type': 'productType'
    }

    def __init__(self, product_family=None, product_series=None, product_type=None):  # noqa: E501
        """TemplateDTODeviceTypes - a model defined in Swagger"""  # noqa: E501

        self._product_family = None
        self._product_series = None
        self._product_type = None
        self.discriminator = None

        if product_family is not None:
            self.product_family = product_family
        if product_series is not None:
            self.product_series = product_series
        if product_type is not None:
            self.product_type = product_type

    @property
    def product_family(self):
        """Gets the product_family of this TemplateDTODeviceTypes.  # noqa: E501


        :return: The product_family of this TemplateDTODeviceTypes.  # noqa: E501
        :rtype: str
        """
        return self._product_family

    @product_family.setter
    def product_family(self, product_family):
        """Sets the product_family of this TemplateDTODeviceTypes.


        :param product_family: The product_family of this TemplateDTODeviceTypes.  # noqa: E501
        :type: str
        """

        self._product_family = product_family

    @property
    def product_series(self):
        """Gets the product_series of this TemplateDTODeviceTypes.  # noqa: E501


        :return: The product_series of this TemplateDTODeviceTypes.  # noqa: E501
        :rtype: str
        """
        return self._product_series

    @product_series.setter
    def product_series(self, product_series):
        """Sets the product_series of this TemplateDTODeviceTypes.


        :param product_series: The product_series of this TemplateDTODeviceTypes.  # noqa: E501
        :type: str
        """

        self._product_series = product_series

    @property
    def product_type(self):
        """Gets the product_type of this TemplateDTODeviceTypes.  # noqa: E501


        :return: The product_type of this TemplateDTODeviceTypes.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this TemplateDTODeviceTypes.


        :param product_type: The product_type of this TemplateDTODeviceTypes.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

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
        if not isinstance(other, TemplateDTODeviceTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
