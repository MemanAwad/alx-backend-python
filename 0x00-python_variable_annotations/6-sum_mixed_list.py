#!/usr/bin/env python3
from typing import List
from typing import Union
"""type-annotated function sum_mixed_list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of integers and floats and returns their sum as a float"""
    return float(sum(mxd_lst))
