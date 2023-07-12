import asyncio 
import time

async def task_coro(value):
    print(f'{time.ctime()} task {value} executing')
    await asyncio.sleep(1)

async def main():
    print(f'{time.ctime()} main starting.') 
    coros = [task_coro(i) for i in range(10)]
    await asyncio.gather(*coros)
    print(f'{time.ctime()} main done')

asyncio.run(main())



# - /Users/yannapatsakanupong/Desktop/Asynchronous\ /Asyncronus-4.py 
        # Wed Jul 12 22:31:28 2023 main starting.
        # Wed Jul 12 22:31:28 2023 task 0 executing
        # Wed Jul 12 22:31:28 2023 task 1 executing
        # Wed Jul 12 22:31:28 2023 task 2 executing
        # Wed Jul 12 22:31:28 2023 task 3 executing
        # Wed Jul 12 22:31:28 2023 task 4 executing
        # Wed Jul 12 22:31:28 2023 task 5 executing
        # Wed Jul 12 22:31:28 2023 task 6 executing
        # Wed Jul 12 22:31:28 2023 task 7 executing
        # Wed Jul 12 22:31:28 2023 task 8 executing
        # Wed Jul 12 22:31:28 2023 task 9 executing
        # Wed Jul 12 22:31:29 2023 main done