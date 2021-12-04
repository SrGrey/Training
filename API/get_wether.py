import requests


''' script for get weather using place's latitude and longitude from Google map
API GET-request example https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely'''

URL_API = 'https://api.weatherbit.io/v2.0/'
API_KEY = 'API KEY' #please register on https://api.weatherbit.io/ and past here your personal API KEY

lat, lon = input('Right click on place in Google maps, copy the first string with latitude and longitude and past it here').split(',')
lon = lon.strip()

current_weather_url = f"{URL_API}current?lat={lat}&lon={lon}&key={API_KEY}&include=minutely"
current_weather = requests.get(current_weather_url)
if current_weather.status_code == 200:
    response = current_weather.json()
    result_temperature = response['data'][0]['temp']
    print(f'Temperature in this place is aprox: {result_temperature} ºC')
else:
    print('Something went wrong')
