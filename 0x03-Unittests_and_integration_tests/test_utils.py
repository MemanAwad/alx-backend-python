#!/usr/bin/env python3
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map
'''testing the util file'''


class TestAccessNestedMap(unittest.TestCase):
    '''class for testing the access nested map function'''
    @parameterized.expand([({"a": 1},("a",), 1),
    ({"a": {"b": 2}}, ("a",), {'b': 2}),
    ({"a": {"b": 2}}, ("a", "b"), 2),])
    def test_access_nested_map(self, nested_map, path, expected):
        '''testing method for access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
