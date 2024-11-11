from random import random, randint
import time
import multiprocessing

def take_poll(user,votes):
   time.sleep(random())
   vote = randint(1,votes)
   return print(f"Пользователь {user+1} выбрал: {vote} пункт")

def multiprocessing_main():
    processes = []
    votes = 3
    time_start = time.time()
    for i in range(2000):
        process = multiprocessing.Process(target=take_poll, args=(i,votes))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    time_end = time.time()
    print(f'Время, затраченное на выполнение программы с использованием Multiprocessing:, '
          f'{time_end - time_start} сек.')  # фиксация времени на получение результатов: 2.92 секунд

if __name__ == '__main__':
    multiprocessing_main()
