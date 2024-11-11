import multiprocessing
import time
from get_weather import get_weather
from cities import cities

'''
Необходимые нам библиотеки: multiprocessing - для запуска асинхронных функций
                            time - для фиксирования времени выполнения программы
                            requests - для получения запросов http
'''


def multiprocessing_main(cities): #тело программы, управление пулами процессов
    time_start = time.time()
    with multiprocessing.Pool(processes=16) as pool:
        results = pool.map(get_weather, cities)
    time_end = time.time()
    print(f'Время, затраченное на выполнение программы с использованием Multiprocessing:, '
          f'{time_end - time_start} сек.')  # фиксация времени на получение результатов: 2.92 секунд
    return results


if __name__ == '__main__':
    multiprocessing_main(cities) #запуск основной функции


