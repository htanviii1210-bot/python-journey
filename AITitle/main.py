from groq import Groq
from prompts import title_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("========== AI TITLE GENERATOR ==========")
while True:
    print("\n1.Generate a Title\n2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        print("Enter ur paragraph")
        print("Type END once ur done pasting!")
        fullpara = []
        while True:
            para = input()
            if para == "END":
                break
            fullpara.append(para)
        fullpara = "\n".join(fullpara)
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role" : "system",
                    "content" : title_prompt
                },
                {
                    "role" : "user",
                    "content" : fullpara
                }

            ]
        )
        print("=================TITLES=================")
        print(response.choices[0].message.content)
    else:
        print("Invalid Input!")