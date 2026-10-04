import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Groq API
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit page
st.title("🤖 AI Chatbot")
st.caption("Powered by Groq")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("💬 Chat History")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.sidebar.write("👤", message["content"])
    elif message["role"] == "assistant":
        st.sidebar.write("🤖", message["content"])

# Old messages show karna
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_message = st.chat_input("Type your message...")

if user_message:

    # User message
    st.chat_message("user").write(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    # AI response
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ] + st.session_state.messages
    )

    answer = response.choices[0].message.content

    # Bot message
    st.chat_message("assistant").write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })