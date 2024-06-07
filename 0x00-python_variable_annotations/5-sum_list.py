#!/usr/bin/env python3
from typing import List
"""type-annotated function sum_list"""


def sum_list(input_list: list[float]) -> float:
    """takes a list of floats as argument and returns their sum as a float"""
    sum: float = 0.0
    for x in input_list:
        sum += x
    return sum
