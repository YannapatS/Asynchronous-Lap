#example of using asyncio shield to protect a task from cacellation
import time
import asyncio

#define a simple asynchronous
async def simple_task(number):
    #block for a moment
    await asyncio.sleep(1)
    #return the argument
    return number 

#cancel the given task after a moment
async def cancel_task(task):
    #block for a moment
    await asyncio.sleep(0.2)
    #cancel the task
    was_canceled = task.cancel()
    print(f'{time.ctime()} canceled: {was_canceled}')

#define a simple corotine
async def main():
    #create the corotine
    coro = simple_task(1)
    #create a task
    task = asyncio.create_task(coro)
    #create the sheild task
    shieled = asyncio.shield(task)
    #create the task to cancel the previous task
    asyncio.create_task(cancel_task(shieled))
    #handle cancellation
    try:
        #await the shielded task
        result = await shieled
        print(f'{time.ctime()} >got: {result}')
    #wait a moment
    except asyncio.CancelledError:
        print(f'{time.ctime()} shieled was cancel')
    #report the details of the tasks
    await asyncio.sleep(1)
    
    print(f'{time.ctime()} shielded: {shielded}')
    print(f'{time.ctime()} task: {task}')

#start the loop
asyncio.run(main())

# - /Users/yannapatsakanupong/Desktop/Asynchronous\ /Asyncronus-7.py 
        # Wed Jul 12 22:33:55 2023 canceled: True
        # Wed Jul 12 22:33:55 2023 shieled was cancel