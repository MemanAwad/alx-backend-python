#!/usr/bin/env python3
''' random modoule'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random delay between 0 and max_delay'''
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return(rand)
