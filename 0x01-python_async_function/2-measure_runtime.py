#!/usr/bin/env python3
"""measure runtime module"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """measure_time: measures the total execution time for wait_n(n, max_delay)
    and returns it"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
