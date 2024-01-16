#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    delays = []
    for i in range(n):
        time = await wait_random(max_delay)
        delays.append(time)
    return sorted(delays)