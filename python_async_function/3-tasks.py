#!/usr/bin/env python3
"""Module for creating asyncio tasks from coroutines."""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task for wait_random coroutine.

    This function wraps the wait_random coroutine into a Task object,
    which allows it to be scheduled concurrently in an event loop.

    Args:
        max_delay (int): Maximum delay value in seconds for wait_random

    Returns:
        asyncio.Task: Task object for the wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
