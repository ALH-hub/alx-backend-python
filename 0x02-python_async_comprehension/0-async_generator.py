#!/usr/bin/env python3
"""async generator"""
import random
import asyncio


async def async_generator():
    """async generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
