#!/usr/bin/env python3
"""This module provides asynchronous coroutines for
measuring concurrent execution runtime."""

import asyncio
import time

async_comprehension = __import__
("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime of executing async_comprehension
    four times concurrently.

    Returns:
        float: Total execution time in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time.time() - start_time
