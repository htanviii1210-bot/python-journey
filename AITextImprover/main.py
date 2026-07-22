from groq import Groq
from dotenv import load_dotenv
from prompts import improved_prompt
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("========== AI TEXT IMPROVER ==========")

while True:
    print("1. Improve Text")
    print("2. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        text = []
        while True:
            line = input("Paste your text.Type END on a new line when finished.")
            if line == "END":
                break;
            text.append(line)
        text = "\n".join(text)
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role" : "system",
                    "content" : improved_prompt
                },
                {
                    "role" : "user",
                    "content" : text
                }
            ]
        )
        print("\n===== Improved Text =====\n")
        print(response.choices[0].message.content)
    else:
        print("Invalid Input!")

        