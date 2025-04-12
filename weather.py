import requests

API_KEY = "b1b15e88fa797225412429c1c50c122a1"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print("\n🌤 Weather Report 🌤")
        print(f"📍 City: {data['name']}, {data['sys']['country']}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"☁ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("\n❌ City not found! Please enter a valid city name.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)