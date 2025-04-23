#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a specified multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns its product with the multiplier.
    """

    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
