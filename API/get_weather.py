import requests
def get_weather(city):    #функция, используя API получает данные с сайта и выводит нам погоду
    url = f'http://api.weatherapi.com/v1/current.json'
    params = {'q': city, 'lang': 'RU', 'key': 'ab11e54d50a04ac29f7143903243110'}
    response = requests.get(url=url, params=params)
    weather = response.json()
    print(f'Город: {weather['location']['name']} ({weather['location']['country']}), '
            f'{weather['current']['condition']['text']}, '
            f'температура {weather['current']['temp_c']} \u00B0C, '
            f'ощущается как {weather['current']['feelslike_c']} \u00B0C')