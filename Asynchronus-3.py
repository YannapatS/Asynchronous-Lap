#example of staring many tasks and getting access yo all tasks
import asyncio
import time

#coroutine for a task
async def task_coroutine(value):
    #report a message
    print(f'{time.ctime()} task {value} is running')
    #block for a moment
    await asyncio.sleep(1)

#define a main coroutine
async def main():
    #report a message
    print(f'{time.ctime()} main coroutin started')
    #start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    #allow some of the taske time to start
    await asyncio.sleep(0.1)
    #get alll tasks
    tasks = asyncio.all_tasks()
    #report all tasks
    for task in tasks:
        print(f'{time.ctime()} > {task.get_name()}, {task.get_coro()}')
    #wait for all tasks to complete
    for task in started_tasks:
        await task
#start the asyncio program
asyncio.run(main())

# Users/yannapatsakanupong/Desktop/Asynchronous\ /Asynchronus-3.py 
        # Wed Jul 12 22:22:34 2023 main coroutin started
        # Wed Jul 12 22:22:34 2023 task 0 is running
        # Wed Jul 12 22:22:34 2023 task 1 is running
        # Wed Jul 12 22:22:34 2023 task 2 is running
        # Wed Jul 12 22:22:34 2023 task 3 is running
        # Wed Jul 12 22:22:34 2023 task 4 is running
        # Wed Jul 12 22:22:34 2023 task 5 is running
        # Wed Jul 12 22:22:34 2023 task 6 is running
        # Wed Jul 12 22:22:34 2023 task 7 is running
        # Wed Jul 12 22:22:34 2023 task 8 is running
        # Wed Jul 12 22:22:34 2023 task 9 is running
        # Wed Jul 12 22:22:34 2023 > Task-6, <coroutine object task_coroutine at 0x10243b2c0>
        # Wed Jul 12 22:22:34 2023 > Task-11, <coroutine object task_coroutine at 0x10243b5c0>
        # Wed Jul 12 22:22:34 2023 > Task-1, <coroutine object main at 0x102369c40>
        # Wed Jul 12 22:22:34 2023 > Task-4, <coroutine object task_coroutine at 0x10243b1c0>
        # Wed Jul 12 22:22:34 2023 > Task-9, <coroutine object task_coroutine at 0x10243b440>
        # Wed Jul 12 22:22:34 2023 > Task-2, <coroutine object task_coroutine at 0x10243b0c0>
        # Wed Jul 12 22:22:34 2023 > Task-7, <coroutine object task_coroutine at 0x10243b340>
        # Wed Jul 12 22:22:34 2023 > Task-5, <coroutine object task_coroutine at 0x10243b240>
        # Wed Jul 12 22:22:34 2023 > Task-10, <coroutine object task_coroutine at 0x10243b4c0>
        # Wed Jul 12 22:22:34 2023 > Task-3, <coroutine object task_coroutine at 0x10243b140>
        # Wed Jul 12 22:22:34 2023 > Task-8, <coroutine object task_coroutine at 0x10243b3c0>*