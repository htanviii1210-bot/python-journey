from groq import Groq
from dotenv import load_dotenv
from prompts import motivation, study, resume, code
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("====== AI MULTI TOOL ======")

while True:
    print("1. Motivation Coach 💪")
    print("2. Study Buddy 📚")
    print("3. Resume Helper 📄")
    print("4. Explain Code 💻")
    print("5. Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 5:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        system_prompt = motivation
    elif ch == 2:
        system_prompt = study
    elif ch == 3:
        system_prompt = resume
    elif ch == 4:
        system_prompt = code
    else:
        print("Invalid Input!")
        continue

    question = input("Enter ur thoughts or queries:")
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role" : "system",
                "content" : system_prompt
            },
            {
                "role" : "user",
                "content" : question
            }
        ]
    )

    print("\n===== AI Response =====\n")
    print(response.choices[0].message.content)
    print("\n")