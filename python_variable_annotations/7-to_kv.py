#!/usr/bin/env python3
"""
This module provides a function to create a tuple containing
a string and the square of a numeric value.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a numeric value.

    Args:
        k (str): The string to be used as the first element of the tuple.
        v (Union[int, float]): A number (integer or float)
        whose square will be the second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the input
        string `k` and the second element is the square of `v` as a float.
    """
    return (k, v**2)
