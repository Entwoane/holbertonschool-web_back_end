#!/usr/bin/env python3
"""
Module for running multiple asynchronous task_wait_random
coroutines concurrently.
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns
    a list of all the delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay value for task_wait_random.

    Returns:
        List[float]: A list of the delays (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
