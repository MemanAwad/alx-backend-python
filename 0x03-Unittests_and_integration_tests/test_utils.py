#!/usr/bin/env python3
'''testing the util file'''

import unittest
from parameterized import parameterized
from utils import (access_nested_map, get_json)
from unittest.mock import patch, MagicMock
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
    def test_get_json(self, test_url, test_payload, mock_get):
        '''function test that utils.get_json returns the expected result.'''
        mock_response  = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.get.return_value = mock_response 
        self.assertEqual(get_json(test_url), test_payload)
        
