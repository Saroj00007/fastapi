import asyncio

async def task1():
    print("performing task 1")
    
    await asyncio.sleep(2)
    
    print("finished task 1")
    
async def task2():
    print("performing task 2")
    
    await asyncio.sleep(2)
    
    print("finished task 2")
    
async def task3():
    print("performing task 3")
    
    await asyncio.sleep(2)
    
    print("finished task 3")
    
    
async def main():
    await asyncio.gather(task1() , task2() , task3())
    
asyncio.run(main())