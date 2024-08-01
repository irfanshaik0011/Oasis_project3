import requests

def get_weather(api_key, location):
    # URL to fetch the weather data
    url = f'http://dataservice.accuweather.com/forecasts/v1/daily/10day

'
    
    # Sending the HTTP request to the API
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        # Extracting required information
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']

        # Displaying the weather information
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print(f"Error: Unable to fetch weather data for {location}. Please check the location and try again.")

def main():
    # Your OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    
    # Taking location input from the user
    location = input("Enter the city name or ZIP code: ")
    
    # Fetching and displaying the weather data