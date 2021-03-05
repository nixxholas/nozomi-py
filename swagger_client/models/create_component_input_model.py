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

class CreateComponentInputModel(object):
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
        'guid': 'str',
        'component_type_id': 'int',
        'identifier': 'str',
        'query': 'str',
        'is_denominated': 'bool',
        'anomaly_ignorance': 'bool',
        'store_historicals': 'bool',
        'request_id': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'component_type_id': 'componentTypeId',
        'identifier': 'identifier',
        'query': 'query',
        'is_denominated': 'isDenominated',
        'anomaly_ignorance': 'anomalyIgnorance',
        'store_historicals': 'storeHistoricals',
        'request_id': 'requestId'
    }

    def __init__(self, guid=None, component_type_id=None, identifier=None, query=None, is_denominated=None, anomaly_ignorance=None, store_historicals=None, request_id=None):  # noqa: E501
        """CreateComponentInputModel - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._component_type_id = None
        self._identifier = None
        self._query = None
        self._is_denominated = None
        self._anomaly_ignorance = None
        self._store_historicals = None
        self._request_id = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if component_type_id is not None:
            self.component_type_id = component_type_id
        if identifier is not None:
            self.identifier = identifier
        if query is not None:
            self.query = query
        if is_denominated is not None:
            self.is_denominated = is_denominated
        if anomaly_ignorance is not None:
            self.anomaly_ignorance = anomaly_ignorance
        if store_historicals is not None:
            self.store_historicals = store_historicals
        if request_id is not None:
            self.request_id = request_id

    @property
    def guid(self):
        """Gets the guid of this CreateComponentInputModel.  # noqa: E501


        :return: The guid of this CreateComponentInputModel.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this CreateComponentInputModel.


        :param guid: The guid of this CreateComponentInputModel.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def component_type_id(self):
        """Gets the component_type_id of this CreateComponentInputModel.  # noqa: E501


        :return: The component_type_id of this CreateComponentInputModel.  # noqa: E501
        :rtype: int
        """
        return self._component_type_id

    @component_type_id.setter
    def component_type_id(self, component_type_id):
        """Sets the component_type_id of this CreateComponentInputModel.


        :param component_type_id: The component_type_id of this CreateComponentInputModel.  # noqa: E501
        :type: int
        """

        self._component_type_id = component_type_id

    @property
    def identifier(self):
        """Gets the identifier of this CreateComponentInputModel.  # noqa: E501


        :return: The identifier of this CreateComponentInputModel.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this CreateComponentInputModel.


        :param identifier: The identifier of this CreateComponentInputModel.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def query(self):
        """Gets the query of this CreateComponentInputModel.  # noqa: E501


        :return: The query of this CreateComponentInputModel.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CreateComponentInputModel.


        :param query: The query of this CreateComponentInputModel.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def is_denominated(self):
        """Gets the is_denominated of this CreateComponentInputModel.  # noqa: E501


        :return: The is_denominated of this CreateComponentInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_denominated

    @is_denominated.setter
    def is_denominated(self, is_denominated):
        """Sets the is_denominated of this CreateComponentInputModel.


        :param is_denominated: The is_denominated of this CreateComponentInputModel.  # noqa: E501
        :type: bool
        """

        self._is_denominated = is_denominated

    @property
    def anomaly_ignorance(self):
        """Gets the anomaly_ignorance of this CreateComponentInputModel.  # noqa: E501


        :return: The anomaly_ignorance of this CreateComponentInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._anomaly_ignorance

    @anomaly_ignorance.setter
    def anomaly_ignorance(self, anomaly_ignorance):
        """Sets the anomaly_ignorance of this CreateComponentInputModel.


        :param anomaly_ignorance: The anomaly_ignorance of this CreateComponentInputModel.  # noqa: E501
        :type: bool
        """

        self._anomaly_ignorance = anomaly_ignorance

    @property
    def store_historicals(self):
        """Gets the store_historicals of this CreateComponentInputModel.  # noqa: E501


        :return: The store_historicals of this CreateComponentInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._store_historicals

    @store_historicals.setter
    def store_historicals(self, store_historicals):
        """Sets the store_historicals of this CreateComponentInputModel.


        :param store_historicals: The store_historicals of this CreateComponentInputModel.  # noqa: E501
        :type: bool
        """

        self._store_historicals = store_historicals

    @property
    def request_id(self):
        """Gets the request_id of this CreateComponentInputModel.  # noqa: E501


        :return: The request_id of this CreateComponentInputModel.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateComponentInputModel.


        :param request_id: The request_id of this CreateComponentInputModel.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

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
        if issubclass(CreateComponentInputModel, dict):
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
        if not isinstance(other, CreateComponentInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other