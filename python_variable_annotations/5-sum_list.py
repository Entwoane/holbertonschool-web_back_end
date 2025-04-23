#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of
a list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements in a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point
        numbers to be summed.

    Returns:
        float: The sum of all elements in the input list.
    """
    return sum(input_list)
