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


class DiscoveryJobNIOListResultResponse(object):
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
        'cli_status': 'str',
        'discovery_status': 'str',
        'end_time': 'str',
        'http_status': 'str',
        'id': 'str',
        'inventory_collection_status': 'str',
        'inventory_reachability_status': 'str',
        'ip_address': 'str',
        'job_status': 'str',
        'name': 'str',
        'netconf_status': 'str',
        'ping_status': 'str',
        'snmp_status': 'str',
        'start_time': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'attribute_info': 'attributeInfo',
        'cli_status': 'cliStatus',
        'discovery_status': 'discoveryStatus',
        'end_time': 'endTime',
        'http_status': 'httpStatus',
        'id': 'id',
        'inventory_collection_status': 'inventoryCollectionStatus',
        'inventory_reachability_status': 'inventoryReachabilityStatus',
        'ip_address': 'ipAddress',
        'job_status': 'jobStatus',
        'name': 'name',
        'netconf_status': 'netconfStatus',
        'ping_status': 'pingStatus',
        'snmp_status': 'snmpStatus',
        'start_time': 'startTime',
        'task_id': 'taskId'
    }

    def __init__(self, attribute_info=None, cli_status=None, discovery_status=None, end_time=None, http_status=None, id=None, inventory_collection_status=None, inventory_reachability_status=None, ip_address=None, job_status=None, name=None, netconf_status=None, ping_status=None, snmp_status=None, start_time=None, task_id=None):  # noqa: E501
        """DiscoveryJobNIOListResultResponse - a model defined in Swagger"""  # noqa: E501

        self._attribute_info = None
        self._cli_status = None
        self._discovery_status = None
        self._end_time = None
        self._http_status = None
        self._id = None
        self._inventory_collection_status = None
        self._inventory_reachability_status = None
        self._ip_address = None
        self._job_status = None
        self._name = None
        self._netconf_status = None
        self._ping_status = None
        self._snmp_status = None
        self._start_time = None
        self._task_id = None
        self.discriminator = None

        if attribute_info is not None:
            self.attribute_info = attribute_info
        if cli_status is not None:
            self.cli_status = cli_status
        if discovery_status is not None:
            self.discovery_status = discovery_status
        if end_time is not None:
            self.end_time = end_time
        if http_status is not None:
            self.http_status = http_status
        if id is not None:
            self.id = id
        if inventory_collection_status is not None:
            self.inventory_collection_status = inventory_collection_status
        if inventory_reachability_status is not None:
            self.inventory_reachability_status = inventory_reachability_status
        if ip_address is not None:
            self.ip_address = ip_address
        if job_status is not None:
            self.job_status = job_status
        if name is not None:
            self.name = name
        if netconf_status is not None:
            self.netconf_status = netconf_status
        if ping_status is not None:
            self.ping_status = ping_status
        if snmp_status is not None:
            self.snmp_status = snmp_status
        if start_time is not None:
            self.start_time = start_time
        if task_id is not None:
            self.task_id = task_id

    @property
    def attribute_info(self):
        """Gets the attribute_info of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The attribute_info of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: object
        """
        return self._attribute_info

    @attribute_info.setter
    def attribute_info(self, attribute_info):
        """Sets the attribute_info of this DiscoveryJobNIOListResultResponse.


        :param attribute_info: The attribute_info of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: object
        """

        self._attribute_info = attribute_info

    @property
    def cli_status(self):
        """Gets the cli_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The cli_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._cli_status

    @cli_status.setter
    def cli_status(self, cli_status):
        """Sets the cli_status of this DiscoveryJobNIOListResultResponse.


        :param cli_status: The cli_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._cli_status = cli_status

    @property
    def discovery_status(self):
        """Gets the discovery_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The discovery_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._discovery_status

    @discovery_status.setter
    def discovery_status(self, discovery_status):
        """Sets the discovery_status of this DiscoveryJobNIOListResultResponse.


        :param discovery_status: The discovery_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._discovery_status = discovery_status

    @property
    def end_time(self):
        """Gets the end_time of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The end_time of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DiscoveryJobNIOListResultResponse.


        :param end_time: The end_time of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def http_status(self):
        """Gets the http_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The http_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this DiscoveryJobNIOListResultResponse.


        :param http_status: The http_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._http_status = http_status

    @property
    def id(self):
        """Gets the id of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The id of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiscoveryJobNIOListResultResponse.


        :param id: The id of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inventory_collection_status(self):
        """Gets the inventory_collection_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The inventory_collection_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._inventory_collection_status

    @inventory_collection_status.setter
    def inventory_collection_status(self, inventory_collection_status):
        """Sets the inventory_collection_status of this DiscoveryJobNIOListResultResponse.


        :param inventory_collection_status: The inventory_collection_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._inventory_collection_status = inventory_collection_status

    @property
    def inventory_reachability_status(self):
        """Gets the inventory_reachability_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The inventory_reachability_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._inventory_reachability_status

    @inventory_reachability_status.setter
    def inventory_reachability_status(self, inventory_reachability_status):
        """Sets the inventory_reachability_status of this DiscoveryJobNIOListResultResponse.


        :param inventory_reachability_status: The inventory_reachability_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._inventory_reachability_status = inventory_reachability_status

    @property
    def ip_address(self):
        """Gets the ip_address of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The ip_address of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DiscoveryJobNIOListResultResponse.


        :param ip_address: The ip_address of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def job_status(self):
        """Gets the job_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The job_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this DiscoveryJobNIOListResultResponse.


        :param job_status: The job_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._job_status = job_status

    @property
    def name(self):
        """Gets the name of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The name of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiscoveryJobNIOListResultResponse.


        :param name: The name of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def netconf_status(self):
        """Gets the netconf_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The netconf_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._netconf_status

    @netconf_status.setter
    def netconf_status(self, netconf_status):
        """Sets the netconf_status of this DiscoveryJobNIOListResultResponse.


        :param netconf_status: The netconf_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._netconf_status = netconf_status

    @property
    def ping_status(self):
        """Gets the ping_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The ping_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._ping_status

    @ping_status.setter
    def ping_status(self, ping_status):
        """Sets the ping_status of this DiscoveryJobNIOListResultResponse.


        :param ping_status: The ping_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._ping_status = ping_status

    @property
    def snmp_status(self):
        """Gets the snmp_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The snmp_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._snmp_status

    @snmp_status.setter
    def snmp_status(self, snmp_status):
        """Sets the snmp_status of this DiscoveryJobNIOListResultResponse.


        :param snmp_status: The snmp_status of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._snmp_status = snmp_status

    @property
    def start_time(self):
        """Gets the start_time of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The start_time of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DiscoveryJobNIOListResultResponse.


        :param start_time: The start_time of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def task_id(self):
        """Gets the task_id of this DiscoveryJobNIOListResultResponse.  # noqa: E501


        :return: The task_id of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DiscoveryJobNIOListResultResponse.


        :param task_id: The task_id of this DiscoveryJobNIOListResultResponse.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

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
        if not isinstance(other, DiscoveryJobNIOListResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
