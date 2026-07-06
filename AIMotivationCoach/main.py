from groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("====== AI Motivation Coach ======")

while True:
    print("1. Talk to AI")
    print("2. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Have a great day ahead!:)")
        break
    elif ch == 1:
        try:
            challenge = input("How are u feeling today?\n")
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                {
                    "role": "system",
                    "content": "You are a kind, practical, motivating coach. Keep responses encouraging, realistic, and under 200 words."
                },
                {
                    "role": "user",
                    "content": challenge
                }
            ]
        )
            print("\n===== AI Coach =====\n")
            print(response.choices[0].message.content)
        except Exception as e:
            print("Error:", e)
    else:
        print("Invalid Input:(")
        