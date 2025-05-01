#!/usr/bin/env python3
"""This module provides asynchronous coroutines for
measuring concurrent execution runtime."""

import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime of executing async_comprehension
    four times concurrently.

    Returns:
        float: Total execution time in seconds.
    """
    start_time = asyncio.get_event_loop().time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
