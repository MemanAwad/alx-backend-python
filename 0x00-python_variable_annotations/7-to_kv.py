#!/usr/bin/env python3
"""type-annotated function to_kv"""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a list of integers and floats and returns their sum as a float"""
    return [k, float(v**2)]
