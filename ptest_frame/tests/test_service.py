"""
Pytest Test Suite for Service Layer Functions with Mocking.

This module contains unit tests for the service-layer functions defined in
`source.service`. The tests focus on validating database access logic and
external API interactions while isolating dependencies using mocks.

Test Coverage:
- Verifies that `get_user_from_db` returns mocked data without accessing
  the real database.
- Validates successful user data retrieval from an external API using
  mocked HTTP responses.
- Ensures proper exception handling when the external API returns an
  error response.

Mocking Strategy:
- unittest.mock.patch is used to replace:
  - `source.service.get_user_from_db` to prevent real database calls.
  - `requests.get` to avoid real HTTP requests to external services.
- Mock objects simulate HTTP response attributes such as status codes
  and JSON payloads.

Pytest Features Used:
- Fixtures via decorators (mock.patch) for dependency injection.
- pytest.raises: To assert that HTTPError exceptions are raised correctly.
- Assertions: To validate expected outcomes.

Dependencies:
- pytest: Test framework.
- unittest.mock: Used for mocking external dependencies.
- requests: HTTP client library (mocked during tests).
- source.service: Module under test.

Assumptions:
- The `get_user` function raises a `requests.HTTPError` when an HTTP
  response status code indicates a failure.
- The `get_user_from_db` function accepts a user ID as input and returns
  a user name.

Notes:
- All external interactions are mocked to ensure tests are deterministic,
  fast, and independent of network or database availability.
- These tests follow unit testing best practices by isolating the
  functionality under test.

Author:
- Test suite maintained by the QA/Automation team.

"""
import pytest
import source.service as service
import unittest.mock as mock
import requests


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_user(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "Leanne Graham"
    }

    mock_get.return_value = mock_response

    data = service.get_user()

    assert data == {"id": 1, "name": "Leanne Graham"}

@mock.patch("requests.get")
def test_get_user_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_user()







