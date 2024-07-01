#!/usr/bin/env python3
'''testing the util file'''

import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)
import requests


class TestAccessNestedMap(unittest.TestCase):
    '''class for testing the access nested map function'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''testing method for access_nested_map'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''test that a KeyError is raised for the wrong input'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''class for testing get_json function'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get_json):
        '''function test that utils.get_json returns the expected result.'''
        mock_get_json.return_value = test_payload
        self.assertEqual(mock_get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''testmemoize class'''

    def test_memoize(self):
        '''test memoixe method'''

        class TestClass:
            '''test class'''
            def a_method(self):
                '''a_method'''
                return 42

            @memoize
            def a_property(self):
                '''memoize method'''
                return self.a_method()

    with patch.object(TestClass, 'a_method') as mock:
        test_class = TestClass()
        test_class.a_property()
        test_class.a_property()
        mock.assert_called_once()
