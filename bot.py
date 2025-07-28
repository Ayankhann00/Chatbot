
from openai import OpenAI
import streamlit as st
from openai import RateLimitError

client = OpenAI(api_key=st.secrets["openai_api_key"])

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
    except Exception as e:
        return f"❌ Error: {str(e)}"
