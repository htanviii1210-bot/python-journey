import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_COUNTRYINFO = os.getenv("API_KEY_COUNTRYINFO")

print("Welcome To The Country Info API App!")
print("====== COUNTRY INFO APP ======")
while True:
    print("\n1. Search Country\n2. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank U!")
        break
    elif ch == 1:
        country = input("Enter the country:")
        response = requests.get(f'https://api.restcountries.com/countries/v5?q={country}',
        headers={'Authorization': f'Bearer {API_KEY_COUNTRYINFO}'})
        response.raise_for_status()
        data = response.json()
        found = False

        for obj in data['data']['objects']:
            if obj['names']['common'].lower() == country.lower():
                countryname = obj['names']['common']
                capital = obj['capitals'][0]['name']
                region = obj['region']
                population = obj['population']

                print(f"Country: {countryname}")
                print(f"Capital: {capital}")
                print(f"Region: {region}")
                print(f"Population: {population}")

                found = True
                break

        if not found:
            print("Country not found!")
    else:
        print("Invalid Input!")