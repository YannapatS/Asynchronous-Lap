import random 
import asyncio
import time

async def task_coro(arg):
    value = random.random()
    await asyncio.sleep(value)
    print(f'{time.ctime()}>task {arg} done with {value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    print(f'{time.ctime()} All done')
    
asyncio.run(main())

# - /Users/yannapatsakanupong/Desktop/Asynchronous\ /Asyncronus-5.py 
        # Wed Jul 12 22:32:32 2023>task 8 done with 0.06573473513105876
        # Wed Jul 12 22:32:32 2023>task 9 done with 0.10130225856493591
        # Wed Jul 12 22:32:32 2023>task 5 done with 0.33013324478682937
        # Wed Jul 12 22:32:32 2023>task 2 done with 0.4092307740442701
        # Wed Jul 12 22:32:33 2023>task 7 done with 0.48427247474052615
        # Wed Jul 12 22:32:33 2023>task 0 done with 0.6123598392009832
        # # Wed Jul 12 22:32:33 2023>task 3 done with 0.6470840172263773
        # # Wed Jul 12 22:32:33 2023>task 4 done with 0.9230107366230882
        # # Wed Jul 12 22:32:33 2023>task 1 done with 0.9293012634956842
        # # Wed Jul 12 22:32:33 2023>task 6 done with 0.9401796356128915
        # # Wed Jul 12 22:32:33 2023 All done