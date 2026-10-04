import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

print("AI Chatbot Started")
print("Type 'exit' to stop")

while True:

    user_message = input("you: ")

    if user_message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant"
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    answer = response.choices[0].message.content

    print("Bot:",answer)
