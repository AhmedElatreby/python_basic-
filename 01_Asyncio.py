'''  
# Synchronous
- Synchronous method are invoked, it completes executing before returning
'''

# an example without asyncio method
import asyncio


# def task1():
#     print('Send First email')
#     print('First email reply')
#     task2()


# def task2():
#     print('Send Secound email')
#     print('Secound email reply')
#     task3()


# def task3():
#     print('Send Third email')
#     print('Third email reply')
#     print('====')
#     print('End')


# task1()

# Same example with Asyncio method


# async def task1():
#     print('Send first email')
#     asyncio.create_task(task2())
#     await asyncio.sleep(4)  # Simulating that the email reply takes 4 secounds
#     print('First email reply')


# async def task2():
#     print('Send secound email')
#     asyncio.create_task(task3())
#     await asyncio.sleep(2)
#     print('Secound email reply')


# async def task3():
#     print('Send third email')
#     await asyncio.sleep(3)
#     print('Third email reply')

# asyncio.run(task1())


'''  
# Coroutines
- Asynchronous function in Python is typically called a (coroutine)
- Coroutines declared with the async / await syntax
- Coroutines are special functions that return coroutine objects when called
'''


# async def send_email():
#     print('hello')
#     await asyncio.sleep(2)
#     print('Awake now')

# check if the function is asynio or not
# print(asyncio.iscoroutinefunction(send_email)) # the outcome is (True)

# asyncio.run(send_email())

# an example for using asyncio function
# it can use to change the order of the programe or the functions

# async def task1():
#     await task2()  # waiting for task 2
#     print('task1')


# async def task2():
#     await task3()  # waiting for task 3
#     print('task2')


# async def task3():
#     await task4()  # waiting for task 4
#     print('task3')


# async def task4():
#     print('task4')

# asyncio.run(task1())

# craet another example for using asyncio function

# async def file_reply():
#     await asyncio.sleep(4)
#     return('file returned')


# async def data_reply():
#     await asyncio.sleep(3)
#     return{"data", 100}


# async def task1():
#     print('Waiting for data....')
#     x = await data_reply()
#     print(x)


# async def task2():
#     print('Waiting for file....')
#     x = await file_reply()
#     print(x)


# async def main():
#     x = asyncio.create_task(task1())
#     y = asyncio.create_task(task2())

#     await x
#     await y


# asyncio.run(main())


'''  
# Event Loop
- The event loop is a very efficient task manager
- Coordinate tasks
- Run asynchronous tasks and callbacks
'''

'''  
Create 3 coroutines named t1, t2 and t3. Each coroutine should print out the name of the coroutine. Call/run the first coroutine and using await have t3 print out first, t2 print out second and t1 print out last. 
'''


async def task1():
    await task2()
    print('Task 1')


async def task2():
    await task3()
    print('Task 2')


async def task3():
    print('Task 3')


asyncio.run(task1())


'''  
Build a coroutine called fetch_data which simulates the collection of data from a network database. Lets assume that takes a few seconds. It should return a dictionary {"data":100}. Next, build a new coroutine which counts down from 10 to 1 (using range). Using await, have each number print to the screen every 2 seconds. Finally build a coroutine called main() and run fetch_data and the countdown coroutine concurrently. Print the data that is returned from fetch_data whilst also counting down from 10.
'''


async def fetch_data():
    print('Fetching data....')
    await asyncio.sleep(2)
    print('Data returend...')
    return {'data': 100}


async def task2():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)


async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(task2())

    data = await x
    print(data)
    await y

asyncio.run(main())
