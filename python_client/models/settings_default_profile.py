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


class SettingsDefaultProfile(object):
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
        'cert': 'str',
        'fqdn_addresses': 'list[str]',
        'ip_addresses': 'list[str]',
        'port': 'int',
        'proxy': 'bool'
    }

    attribute_map = {
        'cert': 'cert',
        'fqdn_addresses': 'fqdnAddresses',
        'ip_addresses': 'ipAddresses',
        'port': 'port',
        'proxy': 'proxy'
    }

    def __init__(self, cert=None, fqdn_addresses=None, ip_addresses=None, port=None, proxy=None):  # noqa: E501
        """SettingsDefaultProfile - a model defined in Swagger"""  # noqa: E501

        self._cert = None
        self._fqdn_addresses = None
        self._ip_addresses = None
        self._port = None
        self._proxy = None
        self.discriminator = None

        if cert is not None:
            self.cert = cert
        if fqdn_addresses is not None:
            self.fqdn_addresses = fqdn_addresses
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if port is not None:
            self.port = port
        if proxy is not None:
            self.proxy = proxy

    @property
    def cert(self):
        """Gets the cert of this SettingsDefaultProfile.  # noqa: E501


        :return: The cert of this SettingsDefaultProfile.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this SettingsDefaultProfile.


        :param cert: The cert of this SettingsDefaultProfile.  # noqa: E501
        :type: str
        """

        self._cert = cert

    @property
    def fqdn_addresses(self):
        """Gets the fqdn_addresses of this SettingsDefaultProfile.  # noqa: E501


        :return: The fqdn_addresses of this SettingsDefaultProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._fqdn_addresses

    @fqdn_addresses.setter
    def fqdn_addresses(self, fqdn_addresses):
        """Sets the fqdn_addresses of this SettingsDefaultProfile.


        :param fqdn_addresses: The fqdn_addresses of this SettingsDefaultProfile.  # noqa: E501
        :type: list[str]
        """

        self._fqdn_addresses = fqdn_addresses

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this SettingsDefaultProfile.  # noqa: E501


        :return: The ip_addresses of this SettingsDefaultProfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this SettingsDefaultProfile.


        :param ip_addresses: The ip_addresses of this SettingsDefaultProfile.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def port(self):
        """Gets the port of this SettingsDefaultProfile.  # noqa: E501


        :return: The port of this SettingsDefaultProfile.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SettingsDefaultProfile.


        :param port: The port of this SettingsDefaultProfile.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def proxy(self):
        """Gets the proxy of this SettingsDefaultProfile.  # noqa: E501


        :return: The proxy of this SettingsDefaultProfile.  # noqa: E501
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this SettingsDefaultProfile.


        :param proxy: The proxy of this SettingsDefaultProfile.  # noqa: E501
        :type: bool
        """

        self._proxy = proxy

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
        if not isinstance(other, SettingsDefaultProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
