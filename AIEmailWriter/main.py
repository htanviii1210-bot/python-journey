from groq import Groq
from dotenv import load_dotenv
from prompts import improve_prompts
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("====== AI EMAIL WRITER ======")

while True:
    print("\n1.Write an email\n2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using the app!")
        break
    elif ch == 1:
        print("Paste ur existing email that u want to improve:")
        print("When ur done type END")
        info = []
        while True:
            email = input()
            if email == "END":
                break
            info.append(email)
        info = "\n".join(info)
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
            {
                "role": "system",
                "content": improve_prompts
            },
            {
                "role": "user",
                "content": info
            }
        ]
        )
        print("\n===== Improved Text =====\n")
        print(response.choices[0].message.content)
    else:
        print("Invalid Input!")
