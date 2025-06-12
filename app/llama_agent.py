import openai
import streamlit as st

OPENAI_API_KEY = "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"
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_script_with_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"OpenAI Error: {e}"

