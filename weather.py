import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:

            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            return (
                f"The weather in {city} is {description}. "
                f"The temperature is {temperature} degrees Celsius "
                f"with humidity of {humidity} percent."
            )

        else:
            return f"API Error: {data.get('message', 'Unknown error')}"

    except Exception as e:
        print(e)
        return "Sorry, I couldn't get the weather information."