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

from python_client.models.sava_mapping_profile import SAVAMappingProfile  # noqa: F401,E501
from python_client.models.sava_mapping_sync_result import SAVAMappingSyncResult  # noqa: F401,E501


class SettingsSavaMappingList(object):
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
        'auto_sync_period': 'int',
        'cco_user': 'str',
        'expiry': 'int',
        'last_sync': 'int',
        'profile': 'SAVAMappingProfile',
        'smart_account_id': 'str',
        'sync_result': 'SAVAMappingSyncResult',
        'sync_result_str': 'str',
        'sync_start_time': 'int',
        'sync_status': 'str',
        'tenant_id': 'str',
        'token': 'str',
        'virtual_account_id': 'str'
    }

    attribute_map = {
        'auto_sync_period': 'autoSyncPeriod',
        'cco_user': 'ccoUser',
        'expiry': 'expiry',
        'last_sync': 'lastSync',
        'profile': 'profile',
        'smart_account_id': 'smartAccountId',
        'sync_result': 'syncResult',
        'sync_result_str': 'syncResultStr',
        'sync_start_time': 'syncStartTime',
        'sync_status': 'syncStatus',
        'tenant_id': 'tenantId',
        'token': 'token',
        'virtual_account_id': 'virtualAccountId'
    }

    def __init__(self, auto_sync_period=None, cco_user=None, expiry=None, last_sync=None, profile=None, smart_account_id=None, sync_result=None, sync_result_str=None, sync_start_time=None, sync_status=None, tenant_id=None, token=None, virtual_account_id=None):  # noqa: E501
        """SettingsSavaMappingList - a model defined in Swagger"""  # noqa: E501

        self._auto_sync_period = None
        self._cco_user = None
        self._expiry = None
        self._last_sync = None
        self._profile = None
        self._smart_account_id = None
        self._sync_result = None
        self._sync_result_str = None
        self._sync_start_time = None
        self._sync_status = None
        self._tenant_id = None
        self._token = None
        self._virtual_account_id = None
        self.discriminator = None

        if auto_sync_period is not None:
            self.auto_sync_period = auto_sync_period
        if cco_user is not None:
            self.cco_user = cco_user
        if expiry is not None:
            self.expiry = expiry
        if last_sync is not None:
            self.last_sync = last_sync
        if profile is not None:
            self.profile = profile
        if smart_account_id is not None:
            self.smart_account_id = smart_account_id
        if sync_result is not None:
            self.sync_result = sync_result
        if sync_result_str is not None:
            self.sync_result_str = sync_result_str
        if sync_start_time is not None:
            self.sync_start_time = sync_start_time
        if sync_status is not None:
            self.sync_status = sync_status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if token is not None:
            self.token = token
        if virtual_account_id is not None:
            self.virtual_account_id = virtual_account_id

    @property
    def auto_sync_period(self):
        """Gets the auto_sync_period of this SettingsSavaMappingList.  # noqa: E501


        :return: The auto_sync_period of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._auto_sync_period

    @auto_sync_period.setter
    def auto_sync_period(self, auto_sync_period):
        """Sets the auto_sync_period of this SettingsSavaMappingList.


        :param auto_sync_period: The auto_sync_period of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._auto_sync_period = auto_sync_period

    @property
    def cco_user(self):
        """Gets the cco_user of this SettingsSavaMappingList.  # noqa: E501


        :return: The cco_user of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._cco_user

    @cco_user.setter
    def cco_user(self, cco_user):
        """Sets the cco_user of this SettingsSavaMappingList.


        :param cco_user: The cco_user of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._cco_user = cco_user

    @property
    def expiry(self):
        """Gets the expiry of this SettingsSavaMappingList.  # noqa: E501


        :return: The expiry of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SettingsSavaMappingList.


        :param expiry: The expiry of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._expiry = expiry

    @property
    def last_sync(self):
        """Gets the last_sync of this SettingsSavaMappingList.  # noqa: E501


        :return: The last_sync of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this SettingsSavaMappingList.


        :param last_sync: The last_sync of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._last_sync = last_sync

    @property
    def profile(self):
        """Gets the profile of this SettingsSavaMappingList.  # noqa: E501


        :return: The profile of this SettingsSavaMappingList.  # noqa: E501
        :rtype: SAVAMappingProfile
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this SettingsSavaMappingList.


        :param profile: The profile of this SettingsSavaMappingList.  # noqa: E501
        :type: SAVAMappingProfile
        """

        self._profile = profile

    @property
    def smart_account_id(self):
        """Gets the smart_account_id of this SettingsSavaMappingList.  # noqa: E501


        :return: The smart_account_id of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._smart_account_id

    @smart_account_id.setter
    def smart_account_id(self, smart_account_id):
        """Sets the smart_account_id of this SettingsSavaMappingList.


        :param smart_account_id: The smart_account_id of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._smart_account_id = smart_account_id

    @property
    def sync_result(self):
        """Gets the sync_result of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_result of this SettingsSavaMappingList.  # noqa: E501
        :rtype: SAVAMappingSyncResult
        """
        return self._sync_result

    @sync_result.setter
    def sync_result(self, sync_result):
        """Sets the sync_result of this SettingsSavaMappingList.


        :param sync_result: The sync_result of this SettingsSavaMappingList.  # noqa: E501
        :type: SAVAMappingSyncResult
        """

        self._sync_result = sync_result

    @property
    def sync_result_str(self):
        """Gets the sync_result_str of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_result_str of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._sync_result_str

    @sync_result_str.setter
    def sync_result_str(self, sync_result_str):
        """Sets the sync_result_str of this SettingsSavaMappingList.


        :param sync_result_str: The sync_result_str of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._sync_result_str = sync_result_str

    @property
    def sync_start_time(self):
        """Gets the sync_start_time of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_start_time of this SettingsSavaMappingList.  # noqa: E501
        :rtype: int
        """
        return self._sync_start_time

    @sync_start_time.setter
    def sync_start_time(self, sync_start_time):
        """Sets the sync_start_time of this SettingsSavaMappingList.


        :param sync_start_time: The sync_start_time of this SettingsSavaMappingList.  # noqa: E501
        :type: int
        """

        self._sync_start_time = sync_start_time

    @property
    def sync_status(self):
        """Gets the sync_status of this SettingsSavaMappingList.  # noqa: E501


        :return: The sync_status of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this SettingsSavaMappingList.


        :param sync_status: The sync_status of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOT_SYNCED", "SYNCING", "SUCCESS", "FAILURE"]  # noqa: E501
        if sync_status not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_status` ({0}), must be one of {1}"  # noqa: E501
                .format(sync_status, allowed_values)
            )

        self._sync_status = sync_status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this SettingsSavaMappingList.  # noqa: E501


        :return: The tenant_id of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this SettingsSavaMappingList.


        :param tenant_id: The tenant_id of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def token(self):
        """Gets the token of this SettingsSavaMappingList.  # noqa: E501


        :return: The token of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SettingsSavaMappingList.


        :param token: The token of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def virtual_account_id(self):
        """Gets the virtual_account_id of this SettingsSavaMappingList.  # noqa: E501


        :return: The virtual_account_id of this SettingsSavaMappingList.  # noqa: E501
        :rtype: str
        """
        return self._virtual_account_id

    @virtual_account_id.setter
    def virtual_account_id(self, virtual_account_id):
        """Sets the virtual_account_id of this SettingsSavaMappingList.


        :param virtual_account_id: The virtual_account_id of this SettingsSavaMappingList.  # noqa: E501
        :type: str
        """

        self._virtual_account_id = virtual_account_id

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
        if not isinstance(other, SettingsSavaMappingList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
