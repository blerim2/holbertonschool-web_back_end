#!/usr/bin/env python3
"""
python async
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    a function that waits for a task
    """
    return asyncio.create_task(wait_random(max_delay))
