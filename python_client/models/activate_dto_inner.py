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


class ActivateDTOInner(object):
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
        'activate_lower_image_version': 'bool',
        'device_upgrade_mode': 'str',
        'device_uuid': 'str',
        'distribute_if_needed': 'bool',
        'image_uuid_list': 'list[str]',
        'smu_image_uuid_list': 'list[str]'
    }

    attribute_map = {
        'activate_lower_image_version': 'activateLowerImageVersion',
        'device_upgrade_mode': 'deviceUpgradeMode',
        'device_uuid': 'deviceUuid',
        'distribute_if_needed': 'distributeIfNeeded',
        'image_uuid_list': 'imageUuidList',
        'smu_image_uuid_list': 'smuImageUuidList'
    }

    def __init__(self, activate_lower_image_version=None, device_upgrade_mode=None, device_uuid=None, distribute_if_needed=None, image_uuid_list=None, smu_image_uuid_list=None):  # noqa: E501
        """ActivateDTOInner - a model defined in Swagger"""  # noqa: E501

        self._activate_lower_image_version = None
        self._device_upgrade_mode = None
        self._device_uuid = None
        self._distribute_if_needed = None
        self._image_uuid_list = None
        self._smu_image_uuid_list = None
        self.discriminator = None

        if activate_lower_image_version is not None:
            self.activate_lower_image_version = activate_lower_image_version
        if device_upgrade_mode is not None:
            self.device_upgrade_mode = device_upgrade_mode
        if device_uuid is not None:
            self.device_uuid = device_uuid
        if distribute_if_needed is not None:
            self.distribute_if_needed = distribute_if_needed
        if image_uuid_list is not None:
            self.image_uuid_list = image_uuid_list
        if smu_image_uuid_list is not None:
            self.smu_image_uuid_list = smu_image_uuid_list

    @property
    def activate_lower_image_version(self):
        """Gets the activate_lower_image_version of this ActivateDTOInner.  # noqa: E501


        :return: The activate_lower_image_version of this ActivateDTOInner.  # noqa: E501
        :rtype: bool
        """
        return self._activate_lower_image_version

    @activate_lower_image_version.setter
    def activate_lower_image_version(self, activate_lower_image_version):
        """Sets the activate_lower_image_version of this ActivateDTOInner.


        :param activate_lower_image_version: The activate_lower_image_version of this ActivateDTOInner.  # noqa: E501
        :type: bool
        """

        self._activate_lower_image_version = activate_lower_image_version

    @property
    def device_upgrade_mode(self):
        """Gets the device_upgrade_mode of this ActivateDTOInner.  # noqa: E501


        :return: The device_upgrade_mode of this ActivateDTOInner.  # noqa: E501
        :rtype: str
        """
        return self._device_upgrade_mode

    @device_upgrade_mode.setter
    def device_upgrade_mode(self, device_upgrade_mode):
        """Sets the device_upgrade_mode of this ActivateDTOInner.


        :param device_upgrade_mode: The device_upgrade_mode of this ActivateDTOInner.  # noqa: E501
        :type: str
        """

        self._device_upgrade_mode = device_upgrade_mode

    @property
    def device_uuid(self):
        """Gets the device_uuid of this ActivateDTOInner.  # noqa: E501


        :return: The device_uuid of this ActivateDTOInner.  # noqa: E501
        :rtype: str
        """
        return self._device_uuid

    @device_uuid.setter
    def device_uuid(self, device_uuid):
        """Sets the device_uuid of this ActivateDTOInner.


        :param device_uuid: The device_uuid of this ActivateDTOInner.  # noqa: E501
        :type: str
        """

        self._device_uuid = device_uuid

    @property
    def distribute_if_needed(self):
        """Gets the distribute_if_needed of this ActivateDTOInner.  # noqa: E501


        :return: The distribute_if_needed of this ActivateDTOInner.  # noqa: E501
        :rtype: bool
        """
        return self._distribute_if_needed

    @distribute_if_needed.setter
    def distribute_if_needed(self, distribute_if_needed):
        """Sets the distribute_if_needed of this ActivateDTOInner.


        :param distribute_if_needed: The distribute_if_needed of this ActivateDTOInner.  # noqa: E501
        :type: bool
        """

        self._distribute_if_needed = distribute_if_needed

    @property
    def image_uuid_list(self):
        """Gets the image_uuid_list of this ActivateDTOInner.  # noqa: E501


        :return: The image_uuid_list of this ActivateDTOInner.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_uuid_list

    @image_uuid_list.setter
    def image_uuid_list(self, image_uuid_list):
        """Sets the image_uuid_list of this ActivateDTOInner.


        :param image_uuid_list: The image_uuid_list of this ActivateDTOInner.  # noqa: E501
        :type: list[str]
        """

        self._image_uuid_list = image_uuid_list

    @property
    def smu_image_uuid_list(self):
        """Gets the smu_image_uuid_list of this ActivateDTOInner.  # noqa: E501


        :return: The smu_image_uuid_list of this ActivateDTOInner.  # noqa: E501
        :rtype: list[str]
        """
        return self._smu_image_uuid_list

    @smu_image_uuid_list.setter
    def smu_image_uuid_list(self, smu_image_uuid_list):
        """Sets the smu_image_uuid_list of this ActivateDTOInner.


        :param smu_image_uuid_list: The smu_image_uuid_list of this ActivateDTOInner.  # noqa: E501
        :type: list[str]
        """

        self._smu_image_uuid_list = smu_image_uuid_list

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
        if not isinstance(other, ActivateDTOInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
