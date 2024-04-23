#!/usr/bin/env python3
"""
python async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that returns a list of delays
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
