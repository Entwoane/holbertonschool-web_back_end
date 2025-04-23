#!/usr/bin/env python3
"""
This module provides utilities for working with sequences.
Includes a function to pair each element of an iterable with its length.
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element from
    the input iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequence elements (such as strings, lists, or tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each
        containing an element from the input and its length.
    """
    return [(i, len(i)) for i in lst]
