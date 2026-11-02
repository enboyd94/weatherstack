import requests
import os
import json
import datetime
import argparse

def get_weather_data(city):

    API_KEY = os.environ.get("API_KEY")
    BASE_URL = "http://api.weatherstack.com/current"
    CITY = city

    params = {
        "access_key": API_KEY,
        "query": CITY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S")

    with open(f"data/weather_{timestamp}.json", "w") as f:
        json.dump(data, f)

    with open(f"logs/weather.log", "a") as log_file:
        log_file.write(f"{timestamp} - Fetched weather data for {CITY}\n")

    print(data)

    return "Done"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Get the latest weather data from a city")

    #Define the variable from the terminal
    parser.add_argument("-c", "--city", type = str, help = "The exact name of a city we want to pull weather data from")

    args = parser.parse_args()

    get_weather_data(args.city)