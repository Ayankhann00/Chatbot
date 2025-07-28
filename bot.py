import streamlit as st
from openai import OpenAI, RateLimitError, OpenAIError

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["openai_api_key"])

# Define a function to get response from GPT
def get_gpt_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        return "⚠️ Rate limit reached. Please wait a few seconds and try again."

    except OpenAIError as e:
        return f"❌ OpenAI Error: {str(e)}"

    except Exception as e:
        return f"❌ Unexpected Error: {str(e)}"

# Streamlit UI
st.title("🤖 AI Chatbot")

user_input = st.text_input("Enter your message")

if st.button("Ask"):
    if user_input:
        with st.spinner("Generating response..."):
            reply = get_gpt_response(user_input)
            st.markdown(f"**Chatbot:** {reply}")
    else:
        st.warning("Please enter a message to ask.")

