from groq import Groq
from pypdf import PdfReader
from prompts import summary_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("========== AI PDF SUMMARIZER ==========")


all_text = ""

while True:
    print("\n1.PDF Reader\n2.Exit")
    ch = int(input("Enter a choice:"))
    if ch == 2:
        print("Thank u for using the app!")
        break
    elif ch == 1:
        filename = input("Enter PDF filename: ")
        reader = PdfReader(filename)
        all_text = ""
        for i in range(len(reader.pages)): 
            page = reader.pages[i]
            text = page.extract_text()
            all_text += text
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {
                    "role" : "system",
                    "content" : summary_prompt
                },
                {
                    "role" : "user",
                    "content" : all_text
                }
            ]
        )
        print("=================================SUMMARY==================================")
        print(response.choices[0].message.content)
    else:
        print("Invalid Input!")