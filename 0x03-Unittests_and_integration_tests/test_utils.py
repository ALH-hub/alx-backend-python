#!/usr/bin/env python3
"""test for utils.access_nested_map"""
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""
    def test_access_nested_map(self):
        """Test access_nested_map function."""
        nested_map = {"a": 1}
        self.assertEqual(access_nested_map(nested_map, ("a",)), 1)
        nested_map = {"a": {"b": 2}}
        self.assertEqual(access_nested_map(nested_map, ("a",)), 2)
        nested_map = {"a": {"b": 2}}
        self.assertEqual(access_nested_map(nested_map, ("a", "b")), 2)


if __name__ == "__main__":
    unittest.main()
