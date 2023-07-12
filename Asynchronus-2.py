#example of getting the current task from the main coroutine
import asyncio

#define a main coroutine
async def main():
    #Report a message
    print('main coroutine started')
    #Get the current task
    task = asyncio.current_task()
    #Report its details
    print(task)

#start the asyncio program
asyncio.run(main())