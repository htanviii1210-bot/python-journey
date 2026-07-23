from groq import Groq
from dotenv import load_dotenv
from prompts import hashtag_prompts
import os

load_dotenv()
client = Groq(api_key = os.getenv("GROQ_API_KEY"))
print("======== AI HASHTAG GENERATOR ========")

while True:
    print("\n1.Generate Hashtags\n2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        print("Enter ur linkedin post paragraph")
        print("Type END once ur done pasting!")
        info = []
        while True:
            post = input()
            if post == "END":
                break
            info.append(post)
        info = "\n".join(info)
        response = client.chat.completions.create(
                model = "llama-3.3-70b-versatile",
                messages = [
                    {
                        "role" : "system",
                        "content" : hashtag_prompts
                    },
                    {
                        "role" : "user",
                        "content" : info
                    }
                ]
        )
        print("=================================")
        print("HashTags Created!!!")
        print(response.choices[0].message.content)
    else:
        print("Invalid Input!")