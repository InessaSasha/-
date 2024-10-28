import time
import asyncio

async def inverse_proportional(value, power):
  #высчитываем задержку
  if value == 0:
    return float('inf')
  return 1 / (value ** power)

async def start_strongman(name, power, numb_balls=5):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, numb_balls + 1):
        timesleep = await inverse_proportional(power, 2)
        await asyncio.sleep(timesleep)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    print('Начнём соревнования')
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apolon', 5))
    await task1
    await task2
    await task3
    print('Соревнования окончены')

if __name__ == '__main__':
    asyncio.run(start_tournament())

