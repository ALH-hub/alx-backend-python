#!/usr/bin/env python3
"""concurrent coroutines module"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """wait_n: waits for a random delay between 0 and max_delay
    seconds and returns it n times"""
    delays = [wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
