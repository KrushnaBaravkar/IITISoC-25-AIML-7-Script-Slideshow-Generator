import openai
import streamlit as st

openai.api_key = st.secrets.get("OPENAI_API_KEY",None)

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

