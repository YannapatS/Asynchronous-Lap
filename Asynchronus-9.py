import asyncio
import time

#define an asynchronus iterator
class AsyncIterator():
    #constructor, define some state
    def __init__(self):
        self.counter = 0

    #create an instance of the iterator
    def __aiter__(self):
        return self
    
    #return the next awaitable
    async def __anext__(self):
        #check for no furture items
        if self.counter >= 10:
            raise StopAsyncIteration
        #increment the counter
        self.counter += 1
        #simulate work
        await asyncio.sleep(1)
        #return the counter value
        return self.counter

#main coroutine   
async def main():
    #loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(f'{time.ctime()} {item}')
#execute the asyncio program
asyncio.run(main())    

# Wed Jul 19 13:52:37 2023 1
# Wed Jul 19 13:52:38 2023 2
# Wed Jul 19 13:52:39 2023 3
# Wed Jul 19 13:52:40 2023 4
# Wed Jul 19 13:52:41 2023 5
# Wed Jul 19 13:52:42 2023 6
# Wed Jul 19 13:52:43 2023 7
# Wed Jul 19 13:52:44 2023 8
# Wed Jul 19 13:52:45 2023 9
# Wed Jul 19 13:52:46 2023 10