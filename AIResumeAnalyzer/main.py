from groq import Groq
from dotenv import load_dotenv
from prompts import resume_prompt
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("====== AI RESUME ANALYZER ======")
info = []
while True:
    print("1.Analyze Resume")
    print("2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        print("Paste your resume.")
        print("Type END on a new line when finished.")
        info = []
        try:
            while True:
                line = input()

                if line == "END":
                    break
                info.append(line)
            resume_text = "\n".join(info)
            response = client.chat.completions.create(
                model = "llama-3.3-70b-versatile",
                messages=[
                    {
                        "role" : "system",
                        "content" : resume_prompt
                    },
                    {
                        "role" : "user",
                        "content" : resume_text
                    }
                ]
            )
            print("\n===== Resume Analysis =====\n")
            print(response.choices[0].message.content)
        except Exception as e:
            print("Error:",e)
        
    else:
        print("Invalid Input!")