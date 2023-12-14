# Omar Gomez 12/13/2023
class CityWeather:
    def __init__(self, humidity, temp, temp_max, temp_min, city_name):
        self.humidity = humidity
        self.temp = temp
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.city_name = city_name

    def __str__(self):
        return f'{self.city_name} - Temperature: {self.temp}°C, Humidity: {self.humidity}%'

    def __eq__(self, other):
        return self.temp == other.temp

    def __lt__(self, other):
        return self.temp < other.temp

    def __gt__(self, other):
        return self.temp > other.temp

def main():
    city1 = CityWeather(65, 25, 30, 20, "Example City")
    city2 = CityWeather(70, 28, 32, 22, "Another City")

    print(city1)
    print(city2)

    if city1 == city2:
        print("The temperatures are equal.")
    elif city1 < city2:
        print(f"{city1.city_name} is colder than {city2.city_name}.")
    else:
        print(f"{city1.city_name} is warmer than {city2.city_name}.")

if __name__ == '__main__':
    main()
