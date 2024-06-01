#!/usr/bin/env python3
"""test for utils.access_nested_map"""
import unittest.mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
import unittest
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"za": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map function."""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function."""
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload
        with unittest.mock.patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(test_url), test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test memoize function."""
    def test_memoize(self):
        """Test memoize function."""
        class TestClass:
            """Test class."""
            def a_method(self):
                """A method."""
                return 42

            @memoize
            def a_method_memoized(self):
                """A memoized method."""
                return self.a_method()

        with unittest.mock.patch.object(TestClass, 'a_method',
                                        return_value=42) as mocked:
            tc = TestClass()
            result = tc.a_method_memoized
            result = tc.a_method_memoized
            self.assertEqual(result, 42)
            mocked.assert_called_once()


if __name__ == "__main__":
    unittest.main()
