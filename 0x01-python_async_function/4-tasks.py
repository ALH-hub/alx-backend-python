#!/usr/bin/env python3
"""concurrent coroutines module"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n: waits for a random delay between 0 and max_delay
    seconds and returns it n times"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)

    return delays
