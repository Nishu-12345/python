import requests

# OpenWeatherMap API key
API_KEY = 'd4a3f79d9e0eeb105bdebe63c7d32f75'  # Replace with your actual API key

# Function to get weather information
def get_weather(city):
    # URL to call the OpenWeatherMap API with the city and API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={API_KEY}&units=metric"  # units=metric for Celsius

    response = requests.get(complete_url)

    # If the response is successful (HTTP status code 200)
    if response.status_code == 200:
        data = response.json()

        # Parse necessary data from the JSON response
        main_data = data['main']
        weather_data = data['weather'][0]
        
        temperature = main_data['temp']
        pressure = main_data['pressure']
        humidity = main_data['humidity']
        description = weather_data['description']
        
        # Print weather details
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    
    # else:
    #     print("City not found or invalid API key.")

# Main function
# def main():
#     while True:
#         city = input("Enter the city name (or 'exit' to quit): ").strip()
        
#         if city.lower() == 'exit':
#             print("Goodbye! Stay safe!")
#             break
        
#         get_weather(city)

# if __name__ == "__main__":
#     main()


# New code for forecast 

def get_forecast(city):    
    
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    complete_url = f"{base_url}?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n5-Day Forecast for {city}:")

        # Show forecast every 12 hours
        for forecast in data['list']:
            time = forecast['dt_txt']
            temp = forecast['main']['temp']
            desc = forecast['weather'][0]['description']

            if "12:00:00" in time or "00:00:00" in time:
                print(f"{time}: {temp}°C, {desc}")

    else:
        print(f"Error fetching forecast: {response.status_code} - {response.json().get('message', 'Unknown error')}")
def main():
            while True:
                choice = input("\nEnter 'weather' for current weather, 'forecast' for 5-day forecast, or 'exit' to quit: ").strip().lower()

                if choice == 'exit':
                    print("Goodbye! 🌈")
                    break
                elif choice in ['weather', 'forecast']:
                     city = input("Enter city name: ").strip()
                     if choice == 'weather':
                        get_weather(city)
                     else:
                        get_forecast(city)
                else:
                         print("Invalid choice. Try again!")
def main():
    while True:
        city = input("Enter the city name (or 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            print("Goodbye! Stay safe!")
            break
        
        get_weather(city)

if __name__ == "__main__":
    main()

