# weather_app.py

import requests

# Set your API Key
API_KEY = 'xxxxxxxxxxxx'  # TODO: Replace with your actual API key

# Base URL for OpenWeatherMap
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

# ...

# Task 1: Iterate Over Zip Codes
def iterate_over_zip_codes(zip_codes):
    for zip_code in zip_codes:
        print(f'Pulling data for zip code: {zip_code}')
        # Task 2: Retrieve Data from Weather API
        data = pull_weather_data(zip_code)
        city_name = data['name']
        print(f'Retrieve information from:[{city_name}] city\n')

# Task 3: Define CityWeather Class
class CityWeather:
    def __init__(self, humidity, temp, temp_max, temp_min, city_name):
        self.humidity = humidity
        self.temp = temp
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.city_name = city_name

    def __str__(self):
        return (f"{self.city_name} with current conditions: {self.city_name} has a temperature of {self.temp}\n"
                f"with a humidity of {self.humidity}\n"
                f"a max temp of {self.temp_max} and a min temp of {self.temp_min}")

# Task 4: Store Weather Objects
def create_city_objects(zip_codes):
    city_objects_collection = []
    for zip_code in zip_codes:
        data = pull_weather_data(zip_code)
        city_name = data['name']
        city_weather = CityWeather(
            humidity=data['main']['humidity'],
            temp=data['main']['temp'],
            temp_max=data['main']['temp_max'],
            temp_min=data['main']['temp_min'],
            city_name=city_name
        )
        city_objects_collection.append(city_weather)
    return city_objects_collection

# Task 5: Calculate the Hottest and Coldest Temperature
def calculate_hottest_and_coldest(city_weather_objects):
    hottest_city = max(city_weather_objects, key=lambda x: x.temp)
    coldest_city = min(city_weather_objects, key=lambda x: x.temp)
    return hottest_city.city_name, coldest_city.city_name

def main():
    zip_file = 'zip_codes.txt'
    zip_codes = read_zip_codes(zip_file)

    iterate_over_zip_codes(zip_codes)

    city_objects_collection = create_city_objects(zip_codes)

    hottest_city, coldest_city = calculate_hottest_and_coldest(city_objects_collection)

    print(f'The hottest city is: {hottest_city}')
    print(f'The coldest city is: {coldest_city}')

if __name__ == '__main__':
    main()
