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

from python_client.models.path_response_result_response_device_statistics_cpu_statistics import PathResponseResultResponseDeviceStatisticsCpuStatistics  # noqa: F401,E501
from python_client.models.path_response_result_response_device_statistics_memory_statistics import PathResponseResultResponseDeviceStatisticsMemoryStatistics  # noqa: F401,E501


class PathResponseResultResponseDeviceStatistics(object):
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
        'cpu_statistics': 'PathResponseResultResponseDeviceStatisticsCpuStatistics',
        'memory_statistics': 'PathResponseResultResponseDeviceStatisticsMemoryStatistics'
    }

    attribute_map = {
        'cpu_statistics': 'cpuStatistics',
        'memory_statistics': 'memoryStatistics'
    }

    def __init__(self, cpu_statistics=None, memory_statistics=None):  # noqa: E501
        """PathResponseResultResponseDeviceStatistics - a model defined in Swagger"""  # noqa: E501

        self._cpu_statistics = None
        self._memory_statistics = None
        self.discriminator = None

        if cpu_statistics is not None:
            self.cpu_statistics = cpu_statistics
        if memory_statistics is not None:
            self.memory_statistics = memory_statistics

    @property
    def cpu_statistics(self):
        """Gets the cpu_statistics of this PathResponseResultResponseDeviceStatistics.  # noqa: E501


        :return: The cpu_statistics of this PathResponseResultResponseDeviceStatistics.  # noqa: E501
        :rtype: PathResponseResultResponseDeviceStatisticsCpuStatistics
        """
        return self._cpu_statistics

    @cpu_statistics.setter
    def cpu_statistics(self, cpu_statistics):
        """Sets the cpu_statistics of this PathResponseResultResponseDeviceStatistics.


        :param cpu_statistics: The cpu_statistics of this PathResponseResultResponseDeviceStatistics.  # noqa: E501
        :type: PathResponseResultResponseDeviceStatisticsCpuStatistics
        """

        self._cpu_statistics = cpu_statistics

    @property
    def memory_statistics(self):
        """Gets the memory_statistics of this PathResponseResultResponseDeviceStatistics.  # noqa: E501


        :return: The memory_statistics of this PathResponseResultResponseDeviceStatistics.  # noqa: E501
        :rtype: PathResponseResultResponseDeviceStatisticsMemoryStatistics
        """
        return self._memory_statistics

    @memory_statistics.setter
    def memory_statistics(self, memory_statistics):
        """Sets the memory_statistics of this PathResponseResultResponseDeviceStatistics.


        :param memory_statistics: The memory_statistics of this PathResponseResultResponseDeviceStatistics.  # noqa: E501
        :type: PathResponseResultResponseDeviceStatisticsMemoryStatistics
        """

        self._memory_statistics = memory_statistics

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
        if not isinstance(other, PathResponseResultResponseDeviceStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
