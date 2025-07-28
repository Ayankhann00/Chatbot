
import streamlit as st
from bot import get_gpt_response

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 ChatGPT-powered Chatbot made by Ayan")

user_input = st.text_input("Enter your message:", "")

if user_input:
    with st.spinner("Thinking..."):
        response = get_gpt_response(user_input)
        st.write("**Chatbot:**", response)

