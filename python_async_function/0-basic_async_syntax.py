#!/usr/bin/env python3
"""
a asynchronous coroutine that takes in an integer argument.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.
    Returns the random delay as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
