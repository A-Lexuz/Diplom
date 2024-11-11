from random import random,randint
import time

def take_poll(user,votes):
   time.sleep(random())
   vote = randint(1,votes)
   return print(f"Пользователь {user+1} выбрал: {vote} пункт")

time_start = time.time()

votes = 3
for i in range(200):
    take_poll(i,votes)

time_end = time.time()

print(f'Время, затраченное на выполнение программы без использования асинхронных функций:, '
      f'{time_end - time_start} сек.')