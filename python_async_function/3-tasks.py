#!/usr/bin/env python3
"""
python async
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    async def wait_random():
        await asyncio.sleep(max_delay)
        print(f"Waited for {max_delay} seconds!")

    return asyncio.create_task(wait_random())
