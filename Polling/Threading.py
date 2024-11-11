from random import random, randint
import time
import threading

def take_poll(user,votes):
   time.sleep(random())
   vote = randint(1,votes)
   return print(f"Пользователь {user+1} выбрал: {vote} пункт")

def threaded_main():
   threads = []
   votes = 3
   for i in range(2000):
      thread = threading.Thread(target=take_poll,args=(i,votes))
      threads.append(thread)
      thread.start()

   for thread in threads:
      thread.join()

time_start = time.time()
threaded_main()
time_end = time.time()
print(f'Время, затраченное на выполнение программы с использованием Threading:, '
      f'{time_end - time_start} сек.') #фиксация времени на получение результатов: 1.07 секунд
