import time
import asyncio
from email.policy import default


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(10/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament(my_function):

    task1 = asyncio.create_task(my_function('Pasha', 3))
    task2 = asyncio.create_task(my_function('Denis', 4))
    task3 = asyncio.create_task(my_function('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament(start_strongman))