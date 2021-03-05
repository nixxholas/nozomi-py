# coding: utf-8

"""
    Nozomi API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.websocket_command_api import WebsocketCommandApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWebsocketCommandApi(unittest.TestCase):
    """WebsocketCommandApi unit test stubs"""

    def setUp(self):
        self.api = WebsocketCommandApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_websocket_command_all_by_request_get(self):
        """Test case for websocket_command_all_by_request_get

        Obtain all of the websocket commands created, relative to the request.  # noqa: E501
        """
        pass

    def test_websocket_command_all_get(self):
        """Test case for websocket_command_all_get

        Obtain all websocket commands you have created/own.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
