
import webbrowser
import requests
from dotenv import load_dotenv
import os 

load_dotenv()

API_SPACE_KEY = os.getenv("API_SPACE_KEY")
print("====== SPACE APP ======")
print("Welcome To The Space App!")

while True:
    print("\n1.Check Image \n2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        url = f"https://api.nasa.gov/planetary/apod?api_key={API_SPACE_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Title:", data["title"])
        print("Date:", data["date"])
        print("Copyright:", data.get("copyright", "Unknown"))
        print("Explanation:", data["explanation"])
        if data["media_type"] == "image":
            webbrowser.open(data["url"])
        else:
            print("Today's APOD is not an image.")
            print(data["url"])
    else:
        print("Invalid Input:(")