import multiprocessing
import time
import requests
from cities import cities
from get_weather import get_weather
'''
Необходимые нам библиотеки: multiprocessing - для запуска асинхронных функций
                            time - для фиксирования времени выполнения программы
                            requests - для получения запросов http
'''

time_start = time.time()
for city in cities:
    get_weather(city)
time_end = time.time()
print(f'Время, без использования асинхронных функций: '
      f'{time_end - time_start} сек.')  # фиксация времени на получение результатов: 2.92 секунд
