import streamlit as st
from bot import get_gpt_response

st.set_page_config(page_title="GenAI Chatbot", layout="centered")
st.title("🤖 GenAI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        st.session_state.history.append(("You", user_input))
        response = get_gpt_response(user_input)
        st.session_state.history.append(("Bot", response))
        st.experimental_rerun()

for sender, message in reversed(st.session_state.history):
    st.markdown(f"**{sender}:** {message}")
