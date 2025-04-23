#!/usr/bin/env python3
"""Module for measuring the average execution time of
asynchronous coroutines."""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per call for wait_n(n, max_delay).

    Uses the time module to calculate elapsed time
    and asyncio to run the coroutine.

    Args:
        n (int): Number of concurrent executions.
        max_delay (int): Maximum delay value for each wait_random call.

    Returns:
        float: Average execution time per task (total_time / n).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
