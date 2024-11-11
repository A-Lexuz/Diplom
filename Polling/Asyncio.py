from random import random, randint
import time
import asyncio

def take_poll(user,votes):
   time.sleep(random())
   vote = randint(1,votes)
   return print(f"Пользователь {user} выбрал: {vote} пункт")


async def async_without_event_loop(): #не работает в асинхронном режиме
   tasks = []
   for i in range(200):
      tasks.append(asyncio.create_task(take_poll(f'User{i}',votes=3)))

   for task in tasks:
      await task

async def async_with_event_loop():
   loop = asyncio.get_event_loop()
   votes = 3
   for user in range(200):
      tasks = [loop.run_in_executor(None, take_poll, user, votes) ]
   return await asyncio.gather(*tasks)

time_start = time.time()
asyncio.run(async_with_event_loop())
time_end = time.time()

print(f'Время, затраченное на выполнение программы с использованием Asyncio:, '
      f'{time_end - time_start} сек.') #фиксация врем