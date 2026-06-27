import requests
print("====== WEATHER APP ======")
print("Welcome To The Weather App!")
API_KEY = input("Enter API key: ")
while True:
    print("\n1.Check Weather \n2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using the Weather App!")
        break
    elif ch == 1:
        city = input("Enter city:")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        country = data["sys"]["country"]
        feelslike = data["main"]["feels_like"]
        condition = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        print(f"City: {city}")
        print(f"Country: {country}")
        print(f"Temperature: {temp}")
        print(f"Feels Like: {feelslike}")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}")
        print(f"Wind Speed: {wind}")
    else:
        print("Invalid Input")
        