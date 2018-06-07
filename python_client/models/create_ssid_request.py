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


class CreateSSIDRequest(object):
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
        'interface_name': 'str',
        'vlan_id': 'float',
        'ssid_name': 'str',
        'wlan_type': 'str',
        'authentication_type': 'str',
        'authentication_server': 'str',
        'passpharse': 'str',
        'traffic_type': 'str',
        'radio_policy': 'str',
        'fast_transition': 'str',
        'enable_fastlane': 'bool',
        'enable_mac_filering': 'bool',
        'enable_broadcast_ssid': 'bool',
        'enable_wlan_band_selection': 'bool',
        'wireless_network_profile_name': 'str',
        'sites_name_hierarchy_to_map_the_profile': 'str',
        'device_name': 'str',
        'site_name_hierarchy_to_map_device_physical_location': 'str',
        'managed_ap_locations': 'str',
        'interface_ip_address': 'str',
        'interface_net_mask_in_cidr_format': 'str',
        'interface_gateway_ip_address': 'str',
        'interface_lag_port_number': 'float',
        'site_name_hierarchy_to_map_ap_physical_location': 'str',
        'ap_names': 'str',
        'rf_profile': 'str'
    }

    attribute_map = {
        'interface_name': 'interfaceName',
        'vlan_id': 'vlanId',
        'ssid_name': 'ssidName',
        'wlan_type': 'wlanType',
        'authentication_type': 'authenticationType',
        'authentication_server': 'authenticationServer',
        'passpharse': 'passpharse',
        'traffic_type': 'trafficType',
        'radio_policy': 'radioPolicy',
        'fast_transition': 'fastTransition',
        'enable_fastlane': 'enableFastlane',
        'enable_mac_filering': 'enableMACFilering',
        'enable_broadcast_ssid': 'enableBroadcastSSID',
        'enable_wlan_band_selection': 'enableWLANBandSelection',
        'wireless_network_profile_name': 'wirelessNetworkProfileName',
        'sites_name_hierarchy_to_map_the_profile': 'sitesNameHierarchyToMapTheProfile',
        'device_name': 'deviceName',
        'site_name_hierarchy_to_map_device_physical_location': 'siteNameHierarchyToMapDevicePhysicalLocation',
        'managed_ap_locations': 'managedAPLocations',
        'interface_ip_address': 'interfaceIPAddress',
        'interface_net_mask_in_cidr_format': 'interfaceNetMaskInCIDRFormat',
        'interface_gateway_ip_address': 'interfaceGatewayIPAddress',
        'interface_lag_port_number': 'interfaceLAGPortNumber',
        'site_name_hierarchy_to_map_ap_physical_location': 'siteNameHierarchyToMapAPPhysicalLocation',
        'ap_names': 'apNames',
        'rf_profile': 'rfProfile'
    }

    def __init__(self, interface_name=None, vlan_id=None, ssid_name=None, wlan_type=None, authentication_type=None, authentication_server=None, passpharse=None, traffic_type=None, radio_policy=None, fast_transition=None, enable_fastlane=None, enable_mac_filering=None, enable_broadcast_ssid=None, enable_wlan_band_selection=None, wireless_network_profile_name=None, sites_name_hierarchy_to_map_the_profile=None, device_name=None, site_name_hierarchy_to_map_device_physical_location=None, managed_ap_locations=None, interface_ip_address=None, interface_net_mask_in_cidr_format=None, interface_gateway_ip_address=None, interface_lag_port_number=None, site_name_hierarchy_to_map_ap_physical_location=None, ap_names=None, rf_profile=None):  # noqa: E501
        """CreateSSIDRequest - a model defined in Swagger"""  # noqa: E501

        self._interface_name = None
        self._vlan_id = None
        self._ssid_name = None
        self._wlan_type = None
        self._authentication_type = None
        self._authentication_server = None
        self._passpharse = None
        self._traffic_type = None
        self._radio_policy = None
        self._fast_transition = None
        self._enable_fastlane = None
        self._enable_mac_filering = None
        self._enable_broadcast_ssid = None
        self._enable_wlan_band_selection = None
        self._wireless_network_profile_name = None
        self._sites_name_hierarchy_to_map_the_profile = None
        self._device_name = None
        self._site_name_hierarchy_to_map_device_physical_location = None
        self._managed_ap_locations = None
        self._interface_ip_address = None
        self._interface_net_mask_in_cidr_format = None
        self._interface_gateway_ip_address = None
        self._interface_lag_port_number = None
        self._site_name_hierarchy_to_map_ap_physical_location = None
        self._ap_names = None
        self._rf_profile = None
        self.discriminator = None

        if interface_name is not None:
            self.interface_name = interface_name
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if ssid_name is not None:
            self.ssid_name = ssid_name
        if wlan_type is not None:
            self.wlan_type = wlan_type
        if authentication_type is not None:
            self.authentication_type = authentication_type
        if authentication_server is not None:
            self.authentication_server = authentication_server
        if passpharse is not None:
            self.passpharse = passpharse
        if traffic_type is not None:
            self.traffic_type = traffic_type
        if radio_policy is not None:
            self.radio_policy = radio_policy
        if fast_transition is not None:
            self.fast_transition = fast_transition
        if enable_fastlane is not None:
            self.enable_fastlane = enable_fastlane
        if enable_mac_filering is not None:
            self.enable_mac_filering = enable_mac_filering
        if enable_broadcast_ssid is not None:
            self.enable_broadcast_ssid = enable_broadcast_ssid
        if enable_wlan_band_selection is not None:
            self.enable_wlan_band_selection = enable_wlan_band_selection
        if wireless_network_profile_name is not None:
            self.wireless_network_profile_name = wireless_network_profile_name
        if sites_name_hierarchy_to_map_the_profile is not None:
            self.sites_name_hierarchy_to_map_the_profile = sites_name_hierarchy_to_map_the_profile
        if device_name is not None:
            self.device_name = device_name
        if site_name_hierarchy_to_map_device_physical_location is not None:
            self.site_name_hierarchy_to_map_device_physical_location = site_name_hierarchy_to_map_device_physical_location
        if managed_ap_locations is not None:
            self.managed_ap_locations = managed_ap_locations
        if interface_ip_address is not None:
            self.interface_ip_address = interface_ip_address
        if interface_net_mask_in_cidr_format is not None:
            self.interface_net_mask_in_cidr_format = interface_net_mask_in_cidr_format
        if interface_gateway_ip_address is not None:
            self.interface_gateway_ip_address = interface_gateway_ip_address
        if interface_lag_port_number is not None:
            self.interface_lag_port_number = interface_lag_port_number
        if site_name_hierarchy_to_map_ap_physical_location is not None:
            self.site_name_hierarchy_to_map_ap_physical_location = site_name_hierarchy_to_map_ap_physical_location
        if ap_names is not None:
            self.ap_names = ap_names
        if rf_profile is not None:
            self.rf_profile = rf_profile

    @property
    def interface_name(self):
        """Gets the interface_name of this CreateSSIDRequest.  # noqa: E501


        :return: The interface_name of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this CreateSSIDRequest.


        :param interface_name: The interface_name of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def vlan_id(self):
        """Gets the vlan_id of this CreateSSIDRequest.  # noqa: E501


        :return: The vlan_id of this CreateSSIDRequest.  # noqa: E501
        :rtype: float
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this CreateSSIDRequest.


        :param vlan_id: The vlan_id of this CreateSSIDRequest.  # noqa: E501
        :type: float
        """

        self._vlan_id = vlan_id

    @property
    def ssid_name(self):
        """Gets the ssid_name of this CreateSSIDRequest.  # noqa: E501


        :return: The ssid_name of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._ssid_name

    @ssid_name.setter
    def ssid_name(self, ssid_name):
        """Sets the ssid_name of this CreateSSIDRequest.


        :param ssid_name: The ssid_name of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._ssid_name = ssid_name

    @property
    def wlan_type(self):
        """Gets the wlan_type of this CreateSSIDRequest.  # noqa: E501


        :return: The wlan_type of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._wlan_type

    @wlan_type.setter
    def wlan_type(self, wlan_type):
        """Sets the wlan_type of this CreateSSIDRequest.


        :param wlan_type: The wlan_type of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._wlan_type = wlan_type

    @property
    def authentication_type(self):
        """Gets the authentication_type of this CreateSSIDRequest.  # noqa: E501


        :return: The authentication_type of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this CreateSSIDRequest.


        :param authentication_type: The authentication_type of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["wpa2_enterprise", "wpa2_personal", "open"]  # noqa: E501
        if authentication_type not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_type` ({0}), must be one of {1}"  # noqa: E501
                .format(authentication_type, allowed_values)
            )

        self._authentication_type = authentication_type

    @property
    def authentication_server(self):
        """Gets the authentication_server of this CreateSSIDRequest.  # noqa: E501


        :return: The authentication_server of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._authentication_server

    @authentication_server.setter
    def authentication_server(self, authentication_server):
        """Sets the authentication_server of this CreateSSIDRequest.


        :param authentication_server: The authentication_server of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._authentication_server = authentication_server

    @property
    def passpharse(self):
        """Gets the passpharse of this CreateSSIDRequest.  # noqa: E501


        :return: The passpharse of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._passpharse

    @passpharse.setter
    def passpharse(self, passpharse):
        """Sets the passpharse of this CreateSSIDRequest.


        :param passpharse: The passpharse of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._passpharse = passpharse

    @property
    def traffic_type(self):
        """Gets the traffic_type of this CreateSSIDRequest.  # noqa: E501


        :return: The traffic_type of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this CreateSSIDRequest.


        :param traffic_type: The traffic_type of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["voicedata", "data"]  # noqa: E501
        if traffic_type not in allowed_values:
            raise ValueError(
                "Invalid value for `traffic_type` ({0}), must be one of {1}"  # noqa: E501
                .format(traffic_type, allowed_values)
            )

        self._traffic_type = traffic_type

    @property
    def radio_policy(self):
        """Gets the radio_policy of this CreateSSIDRequest.  # noqa: E501


        :return: The radio_policy of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._radio_policy

    @radio_policy.setter
    def radio_policy(self, radio_policy):
        """Sets the radio_policy of this CreateSSIDRequest.


        :param radio_policy: The radio_policy of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["0", "1"]  # noqa: E501
        if radio_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `radio_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(radio_policy, allowed_values)
            )

        self._radio_policy = radio_policy

    @property
    def fast_transition(self):
        """Gets the fast_transition of this CreateSSIDRequest.  # noqa: E501


        :return: The fast_transition of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._fast_transition

    @fast_transition.setter
    def fast_transition(self, fast_transition):
        """Sets the fast_transition of this CreateSSIDRequest.


        :param fast_transition: The fast_transition of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADAPTIVE", "ENABLE", "DISABLE"]  # noqa: E501
        if fast_transition not in allowed_values:
            raise ValueError(
                "Invalid value for `fast_transition` ({0}), must be one of {1}"  # noqa: E501
                .format(fast_transition, allowed_values)
            )

        self._fast_transition = fast_transition

    @property
    def enable_fastlane(self):
        """Gets the enable_fastlane of this CreateSSIDRequest.  # noqa: E501


        :return: The enable_fastlane of this CreateSSIDRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_fastlane

    @enable_fastlane.setter
    def enable_fastlane(self, enable_fastlane):
        """Sets the enable_fastlane of this CreateSSIDRequest.


        :param enable_fastlane: The enable_fastlane of this CreateSSIDRequest.  # noqa: E501
        :type: bool
        """

        self._enable_fastlane = enable_fastlane

    @property
    def enable_mac_filering(self):
        """Gets the enable_mac_filering of this CreateSSIDRequest.  # noqa: E501


        :return: The enable_mac_filering of this CreateSSIDRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_mac_filering

    @enable_mac_filering.setter
    def enable_mac_filering(self, enable_mac_filering):
        """Sets the enable_mac_filering of this CreateSSIDRequest.


        :param enable_mac_filering: The enable_mac_filering of this CreateSSIDRequest.  # noqa: E501
        :type: bool
        """

        self._enable_mac_filering = enable_mac_filering

    @property
    def enable_broadcast_ssid(self):
        """Gets the enable_broadcast_ssid of this CreateSSIDRequest.  # noqa: E501


        :return: The enable_broadcast_ssid of this CreateSSIDRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_broadcast_ssid

    @enable_broadcast_ssid.setter
    def enable_broadcast_ssid(self, enable_broadcast_ssid):
        """Sets the enable_broadcast_ssid of this CreateSSIDRequest.


        :param enable_broadcast_ssid: The enable_broadcast_ssid of this CreateSSIDRequest.  # noqa: E501
        :type: bool
        """

        self._enable_broadcast_ssid = enable_broadcast_ssid

    @property
    def enable_wlan_band_selection(self):
        """Gets the enable_wlan_band_selection of this CreateSSIDRequest.  # noqa: E501


        :return: The enable_wlan_band_selection of this CreateSSIDRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_wlan_band_selection

    @enable_wlan_band_selection.setter
    def enable_wlan_band_selection(self, enable_wlan_band_selection):
        """Sets the enable_wlan_band_selection of this CreateSSIDRequest.


        :param enable_wlan_band_selection: The enable_wlan_band_selection of this CreateSSIDRequest.  # noqa: E501
        :type: bool
        """

        self._enable_wlan_band_selection = enable_wlan_band_selection

    @property
    def wireless_network_profile_name(self):
        """Gets the wireless_network_profile_name of this CreateSSIDRequest.  # noqa: E501


        :return: The wireless_network_profile_name of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._wireless_network_profile_name

    @wireless_network_profile_name.setter
    def wireless_network_profile_name(self, wireless_network_profile_name):
        """Sets the wireless_network_profile_name of this CreateSSIDRequest.


        :param wireless_network_profile_name: The wireless_network_profile_name of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._wireless_network_profile_name = wireless_network_profile_name

    @property
    def sites_name_hierarchy_to_map_the_profile(self):
        """Gets the sites_name_hierarchy_to_map_the_profile of this CreateSSIDRequest.  # noqa: E501


        :return: The sites_name_hierarchy_to_map_the_profile of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._sites_name_hierarchy_to_map_the_profile

    @sites_name_hierarchy_to_map_the_profile.setter
    def sites_name_hierarchy_to_map_the_profile(self, sites_name_hierarchy_to_map_the_profile):
        """Sets the sites_name_hierarchy_to_map_the_profile of this CreateSSIDRequest.


        :param sites_name_hierarchy_to_map_the_profile: The sites_name_hierarchy_to_map_the_profile of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._sites_name_hierarchy_to_map_the_profile = sites_name_hierarchy_to_map_the_profile

    @property
    def device_name(self):
        """Gets the device_name of this CreateSSIDRequest.  # noqa: E501


        :return: The device_name of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this CreateSSIDRequest.


        :param device_name: The device_name of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def site_name_hierarchy_to_map_device_physical_location(self):
        """Gets the site_name_hierarchy_to_map_device_physical_location of this CreateSSIDRequest.  # noqa: E501


        :return: The site_name_hierarchy_to_map_device_physical_location of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._site_name_hierarchy_to_map_device_physical_location

    @site_name_hierarchy_to_map_device_physical_location.setter
    def site_name_hierarchy_to_map_device_physical_location(self, site_name_hierarchy_to_map_device_physical_location):
        """Sets the site_name_hierarchy_to_map_device_physical_location of this CreateSSIDRequest.


        :param site_name_hierarchy_to_map_device_physical_location: The site_name_hierarchy_to_map_device_physical_location of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._site_name_hierarchy_to_map_device_physical_location = site_name_hierarchy_to_map_device_physical_location

    @property
    def managed_ap_locations(self):
        """Gets the managed_ap_locations of this CreateSSIDRequest.  # noqa: E501


        :return: The managed_ap_locations of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._managed_ap_locations

    @managed_ap_locations.setter
    def managed_ap_locations(self, managed_ap_locations):
        """Sets the managed_ap_locations of this CreateSSIDRequest.


        :param managed_ap_locations: The managed_ap_locations of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._managed_ap_locations = managed_ap_locations

    @property
    def interface_ip_address(self):
        """Gets the interface_ip_address of this CreateSSIDRequest.  # noqa: E501


        :return: The interface_ip_address of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._interface_ip_address

    @interface_ip_address.setter
    def interface_ip_address(self, interface_ip_address):
        """Sets the interface_ip_address of this CreateSSIDRequest.


        :param interface_ip_address: The interface_ip_address of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._interface_ip_address = interface_ip_address

    @property
    def interface_net_mask_in_cidr_format(self):
        """Gets the interface_net_mask_in_cidr_format of this CreateSSIDRequest.  # noqa: E501


        :return: The interface_net_mask_in_cidr_format of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._interface_net_mask_in_cidr_format

    @interface_net_mask_in_cidr_format.setter
    def interface_net_mask_in_cidr_format(self, interface_net_mask_in_cidr_format):
        """Sets the interface_net_mask_in_cidr_format of this CreateSSIDRequest.


        :param interface_net_mask_in_cidr_format: The interface_net_mask_in_cidr_format of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._interface_net_mask_in_cidr_format = interface_net_mask_in_cidr_format

    @property
    def interface_gateway_ip_address(self):
        """Gets the interface_gateway_ip_address of this CreateSSIDRequest.  # noqa: E501


        :return: The interface_gateway_ip_address of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._interface_gateway_ip_address

    @interface_gateway_ip_address.setter
    def interface_gateway_ip_address(self, interface_gateway_ip_address):
        """Sets the interface_gateway_ip_address of this CreateSSIDRequest.


        :param interface_gateway_ip_address: The interface_gateway_ip_address of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._interface_gateway_ip_address = interface_gateway_ip_address

    @property
    def interface_lag_port_number(self):
        """Gets the interface_lag_port_number of this CreateSSIDRequest.  # noqa: E501


        :return: The interface_lag_port_number of this CreateSSIDRequest.  # noqa: E501
        :rtype: float
        """
        return self._interface_lag_port_number

    @interface_lag_port_number.setter
    def interface_lag_port_number(self, interface_lag_port_number):
        """Sets the interface_lag_port_number of this CreateSSIDRequest.


        :param interface_lag_port_number: The interface_lag_port_number of this CreateSSIDRequest.  # noqa: E501
        :type: float
        """

        self._interface_lag_port_number = interface_lag_port_number

    @property
    def site_name_hierarchy_to_map_ap_physical_location(self):
        """Gets the site_name_hierarchy_to_map_ap_physical_location of this CreateSSIDRequest.  # noqa: E501


        :return: The site_name_hierarchy_to_map_ap_physical_location of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._site_name_hierarchy_to_map_ap_physical_location

    @site_name_hierarchy_to_map_ap_physical_location.setter
    def site_name_hierarchy_to_map_ap_physical_location(self, site_name_hierarchy_to_map_ap_physical_location):
        """Sets the site_name_hierarchy_to_map_ap_physical_location of this CreateSSIDRequest.


        :param site_name_hierarchy_to_map_ap_physical_location: The site_name_hierarchy_to_map_ap_physical_location of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._site_name_hierarchy_to_map_ap_physical_location = site_name_hierarchy_to_map_ap_physical_location

    @property
    def ap_names(self):
        """Gets the ap_names of this CreateSSIDRequest.  # noqa: E501


        :return: The ap_names of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._ap_names

    @ap_names.setter
    def ap_names(self, ap_names):
        """Sets the ap_names of this CreateSSIDRequest.


        :param ap_names: The ap_names of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """

        self._ap_names = ap_names

    @property
    def rf_profile(self):
        """Gets the rf_profile of this CreateSSIDRequest.  # noqa: E501


        :return: The rf_profile of this CreateSSIDRequest.  # noqa: E501
        :rtype: str
        """
        return self._rf_profile

    @rf_profile.setter
    def rf_profile(self, rf_profile):
        """Sets the rf_profile of this CreateSSIDRequest.


        :param rf_profile: The rf_profile of this CreateSSIDRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["LOW", "TYPICAL", "HIGH"]  # noqa: E501
        if rf_profile not in allowed_values:
            raise ValueError(
                "Invalid value for `rf_profile` ({0}), must be one of {1}"  # noqa: E501
                .format(rf_profile, allowed_values)
            )

        self._rf_profile = rf_profile

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
        if not isinstance(other, CreateSSIDRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
