import asyncio
import time
from aiohttp import ClientSession
from cities import cities

'''
Необходимые нам библиотеки: Asyncio - для запуска асинхронных функций
                            time - для фиксирования времени выполнения программы
                            aiohttp - для запуска сессии
'''
async def get_weather(city): #асинхронная функция, используя API получает данные с сайта и выводит нам погоду
    async with ClientSession() as session:
        url = f'http://api.weatherapi.com/v1/current.json'
        params = {'q': city, 'lang': 'RU', 'key': 'ab11e54d50a04ac29f7143903243110'}

        try:
            async with session.get(url=url, params=params) as response:
                weather = await response.json()
                print(f'Город: {weather['location']['name']} ({weather['location']['country']}), '
                      f'{weather['current']['condition']['text']}, '
                      f'температура {weather['current']['temp_c']} \u00B0C, '
                      f'ощущается как {weather['current']['feelslike_c']} \u00B0C')
        except: print(city, 'город не найден, погода недоступна')


async def main(): #тело нашей программы, которая создает список задач (тасков) и последовательно их запускает
    tasks = []
    for city in cities:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task



time_start = time.time()

asyncio.run(main()) #запуск основной функции

time_end = time.time()

print(f'Время, затраченное на выполнение программы с использованием Asyncio:, '
      f'{time_end - time_start} сек.')
