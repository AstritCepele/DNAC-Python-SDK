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


class ImageInfoListResponseApplicableDevicesForImage(object):
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
        'mdf_id': 'str',
        'product_id': 'list[str]',
        'product_name': 'str'
    }

    attribute_map = {
        'mdf_id': 'mdfId',
        'product_id': 'productId',
        'product_name': 'productName'
    }

    def __init__(self, mdf_id=None, product_id=None, product_name=None):  # noqa: E501
        """ImageInfoListResponseApplicableDevicesForImage - a model defined in Swagger"""  # noqa: E501

        self._mdf_id = None
        self._product_id = None
        self._product_name = None
        self.discriminator = None

        if mdf_id is not None:
            self.mdf_id = mdf_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name

    @property
    def mdf_id(self):
        """Gets the mdf_id of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501


        :return: The mdf_id of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501
        :rtype: str
        """
        return self._mdf_id

    @mdf_id.setter
    def mdf_id(self, mdf_id):
        """Sets the mdf_id of this ImageInfoListResponseApplicableDevicesForImage.


        :param mdf_id: The mdf_id of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501
        :type: str
        """

        self._mdf_id = mdf_id

    @property
    def product_id(self):
        """Gets the product_id of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501


        :return: The product_id of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ImageInfoListResponseApplicableDevicesForImage.


        :param product_id: The product_id of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501
        :type: list[str]
        """

        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501


        :return: The product_name of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ImageInfoListResponseApplicableDevicesForImage.


        :param product_name: The product_name of this ImageInfoListResponseApplicableDevicesForImage.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

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
        if not isinstance(other, ImageInfoListResponseApplicableDevicesForImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
