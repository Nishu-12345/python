import requests
import time

# Configuration
API_KEY = "d4a3f79d9e0eeb105bdebe63c7d32f75"
CITY = "New York"
LAT = 40.7128
LON = -74.0060
CHECK_INTERVAL = 60  # in seconds

def get_weather_alerts(lat, lon):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    alerts = data.get("alerts")
    if alerts:
        for alert in alerts:
            print(f"\nWeather Alert: {alert['event']}")
            print(f"Description: {alert['description']}")
            print(f"Effective: {alert['start']}, Expires: {alert['end']}")
    else:
        print("No weather alerts.")

while True:
    print(f"Checking weather alerts for {CITY}...")
    get_weather_alerts(LAT, LON)
    time.sleep(CHECK_INTERVAL)
