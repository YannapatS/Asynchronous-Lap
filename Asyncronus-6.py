from random import random
import asyncio
import time

async def task_coro(arg):
    value = 1 + random()
    print(f'{time.ctime()} >task got {value}')
    await asyncio.sleep(value)
    print(f'{time.ctime()} >task done')

async def main():
    task = task_coro(1)
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print(f'{time.ctime()} Gave up waiting, task canceled')

asyncio.run(main())

# - /Users/yannapatsakanupong/Desktop/Asynchronous\ /Asyncronus-6.py 
        # Wed Jul 12 22:33:26 2023 >task got 1.662529032974768
        # Wed Jul 12 22:33:26 2023 Gave up waiting, task canceled