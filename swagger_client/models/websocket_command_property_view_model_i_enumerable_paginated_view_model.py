# coding: utf-8

"""
    Nozomi API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel(object):
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
        'total_count': 'int',
        'payload': 'list[WebsocketCommandPropertyViewModel]'
    }

    attribute_map = {
        'total_count': 'totalCount',
        'payload': 'payload'
    }

    def __init__(self, total_count=None, payload=None):  # noqa: E501
        """WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel - a model defined in Swagger"""  # noqa: E501
        self._total_count = None
        self._payload = None
        self.discriminator = None
        if total_count is not None:
            self.total_count = total_count
        if payload is not None:
            self.payload = payload

    @property
    def total_count(self):
        """Gets the total_count of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.  # noqa: E501


        :return: The total_count of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.


        :param total_count: The total_count of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def payload(self):
        """Gets the payload of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.  # noqa: E501


        :return: The payload of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.  # noqa: E501
        :rtype: list[WebsocketCommandPropertyViewModel]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.


        :param payload: The payload of this WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel.  # noqa: E501
        :type: list[WebsocketCommandPropertyViewModel]
        """

        self._payload = payload

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
        if issubclass(WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebsocketCommandPropertyViewModelIEnumerablePaginatedViewModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
