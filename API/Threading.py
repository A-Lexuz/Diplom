import threading
from get_weather import get_weather
import time
from cities import cities

'''
Необходимые нам библиотеки: threading - для запуска потоков функций
                            time - для фиксирования времени выполнения программы
                            requests - для получения запросов http
'''

# Основная функция
def threaded_main(cities):  #тело програаммы, запускающее потоки и ожидающее завершения потоков
    threads = []
    for city in cities:
        thread = threading.Thread(target=get_weather, args=(city,))  # Создаем поток для выполнения функции
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


time_start = time.time()
threaded_main(cities)
time_end = time.time()

print(f'Время, затраченное на выполнение программы с использованием Threading:, '
      f'{time_end - time_start} сек.') #фиксация времени на получение результатов: 0.92 секунд
