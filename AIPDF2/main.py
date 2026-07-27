from groq import Groq
from pypdf import PdfReader
from prompts  import pdf_chat_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("=========== AI PDF CHAT ===========")

while True:
    print("\n1.Chat with PDF\n2.Exit")
    ch = int(input("Enter ur choice:"))
    if ch == 2:
        print("Thank u for using this app!")
        break
    elif ch == 1:
        filename = input("Enter the files name:")
        try:
            reader = PdfReader(filename)
        except FileNotFoundError:
            print("File not found!")
            continue
        all_text=""
        question = input("Ask a question about the PDF: ")
        if question.strip() == "":
            print("Please enter a question")
            continue
        for i in range(min(5, len(reader.pages))):
            page = reader.pages[i]
            text = page.extract_text()
            all_text+=text
        response = client.chat.completions.create(
                model = "llama-3.3-70b-versatile",
                messages = [
                {
                "role": "system",
                "content": pdf_chat_prompt
                },
                {
                "role": "user",
                "content": f"""PDF Content:

                {all_text}

                Question:
                {question}
                """
                }
                ]
                )
        print("ANSWER")
        print(response.choices[0].message.content)
    else:
        print("Invalid Input!")