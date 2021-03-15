# -*- coding: utf-8 -*-

from apps.example.tests import mock_data
from djangocli.utils.unittest.testcase import DjangoCliAPITestCase


class ExampleCommonTestView(DjangoCliAPITestCase):
    def test_expected_exception(self):
        response = self.client.post(
            path="/api/v1/example/common/expected_exception/", data=mock_data.API_EXAMPLE_COMMON_EXCEPTION.request_data
        )
        self.assertDataStructure(
            actual_data=response, expected_data=mock_data.API_EXAMPLE_COMMON_EXCEPTION.response_data
        )

    def test_unexpected_exception(self):
        response = self.client.post(
            path="/api/v1/example/common/unexpected_exception/",
            data=mock_data.API_EXAMPLE_COMMON_UN_EXCEPTION.request_data,
        )
        self.assertDataStructure(
            actual_data=response, expected_data=mock_data.API_EXAMPLE_COMMON_UN_EXCEPTION.response_data
        )

    def test_validate_exception(self):
        response = self.client.post(
            path="/api/v1/example/common/validate_exception/",
            data=mock_data.API_EXAMPLE_COMMON_VALIDATE_EXCEPTION.request_data,
        )
        self.assertDataStructure(
            actual_data=response, expected_data=mock_data.API_EXAMPLE_COMMON_VALIDATE_EXCEPTION.response_data
        )
