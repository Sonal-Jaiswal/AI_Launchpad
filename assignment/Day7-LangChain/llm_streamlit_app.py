from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    model="gemini-3.5-flash",
    temperature=0
)

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Enter your prompt")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    response = llm.invoke(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response.content}
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])