#!/usr/bin/env python3
"""
Asynchronous random float generator.

This module provides an asynchronous generator function that yields
random floating-point numbers between 0 and 10, with a 1-second delay
between each yield.
"""

from typing import AsyncIterator
import random
import asyncio


async def async_generator() -> AsyncIterator[float]:
    """
    Asynchronously yield 10 random floats between 0 and 10.

    Each value is yielded after a 1-second asynchronous pause.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        i = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield i
