#!/usr/bin/env python3
"""
Module for asynchronously collecting values from an async generator.

This module provides a function to asynchronously iterate over
an async generator and collect its yielded values into a list.
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects numbers from the async_generator into a list.

    Asynchronously iterates over the async_generator and returns
    a list containing all the values produced by the generator.

    Returns:
        list: A list of floats yielded by async_generator.
    """
    return [i async for i in async_generator()]
