import requests

#1
print(requests.get("http://open-notify.org/"))

TOKEN = '439b92aa90ca2d280ebc4a6f8f3f9d42'
city_name = input('Введите название города:')


def get_weather(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'

    try:
        response = requests.get(url).json()

        weather = f'''
            Температура: {response["main"]["temp"]} °C
            Влажность: {response["main"]["humidity"]} %
            Давление: {response["main"]["pressure"]} мм рт.ст.
            '''

        print(weather)

    except:

        print('\nТакого города нет.')


if __name__ == '__main__':
    get_weather(TOKEN, city_name)
