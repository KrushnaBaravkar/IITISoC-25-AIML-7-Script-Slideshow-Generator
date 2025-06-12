import streamlit as st
import requests

def generate_script_with_huggingface(prompt):
    API_URL = "https://api-inference.huggingface.co/models/openchat/openchat-3.5"
    headers = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 700
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        else:
            return "⚠️ Unexpected response format."
    else:
        return f"❌ Hugging Face API Error: {response.status_code} – {response.text}"


