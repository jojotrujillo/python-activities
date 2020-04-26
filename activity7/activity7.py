'''Activity 7'''
from datetime import datetime
import requests
import pytemperature

# constants for API URL
START_OF_URL = 'https://api.openweathermap.org/data/2.5/weather?q='
API_KEY = '&APPID=01f7fce1533adaa0564af80eda592431'

def assign_json_values_to_dict(fresh_json):
    """
    fresh_json: newly received JSON from API call

    initialize dictionary to return to main()
    assign specific items from fresh_json to keys in dict
    return dict
    """
    weather_info = {'description': '',
                    'temp': 0.0,
                    'pressure': 0.0,
                    'humidity': 0,
                    'temp_min': 0.0,
                    'temp_max': 0.0}

    weather_info['description'] = fresh_json['weather'][0]['description'] # key, list, value
    weather_info['temp'] = pytemperature.k2f(fresh_json['main']['temp']) # conv. kelvin to fahren
    weather_info['pressure'] = fresh_json['main']['pressure'] / 3386 * 100
    # ^^^ divide hpa (pascal) by 3386 to convert to inHg (inches of mercury)
    weather_info['humidity'] = fresh_json['main']['humidity']
    weather_info['temp_min'] = pytemperature.k2f(fresh_json['main']['temp_min'])
    weather_info['temp_max'] = pytemperature.k2f(fresh_json['main']['temp_max'])

    return weather_info

def main():
    """
    print contextual info to user
    prompt for city and state
    send API call
    print results from call
    """
    print('ISQA 3900 Open Weather API\n' +
          datetime.now().strftime('%A, %d %B, %Y')) # weekday, 2-digit-day month, year

    user_choice = 'y'
    while user_choice.lower() == 'y':
        city = input('\nEnter city:\t\t')
        print('Use ISO letter country code like: https://countrycode.org')
        country = input('Enter country code:\t')

        open_weather_json = requests.get(START_OF_URL + city + ',' + country + API_KEY).json()
        weather_dict = assign_json_values_to_dict(open_weather_json)

        print('{:<41s}{:<30s}'.format('Current conditions:', weather_dict['description']) +
              '\n{:<34s}{:>12.2f}'.format('Current Temperature in Fahrenheit:', \
                  weather_dict['temp']) +
              '\n{:<25s}{:>21.2f}'.format('Current pressure in inHg:', weather_dict['pressure']) +
              '\n{:<19s}{:>24d}'.format('Current % humidity:', weather_dict['humidity']) +
              '\n{:<39s}{:>7.2f}'.format('Expected low temperature in Fahrenheit:', \
                  weather_dict['temp_min']) +
              '\n{:<40s}{:>6.2f}'.format('Expected high temperature in Fahrenheit:', \
                  weather_dict['temp_max']))
        # ^^^ explicit string output formatting using format() to console

        user_choice = input('Continue (y/n)?:\t')

    print('\nBye')

if __name__ == '__main__':
    main()
