#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list
containing both integers and floating-point numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all elements in a list of integers
    and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers
        and/or floating-point numbers to be summed.

    Returns:
        float: The sum of all elements in the input list
        as a floating-point number.
    """
    return sum(mxd_lst)
