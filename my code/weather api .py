import requests

def get_weather(city):
    API_KEY = "265596"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # for Celsius
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print("\n🌦️ Weather Report:")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("❌ City not found! Please enter a valid city name.")

def main():
    print("=== 🌍 Python Weather Forecast App ===")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
