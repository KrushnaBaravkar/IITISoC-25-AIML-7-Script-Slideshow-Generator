import streamlit as st
import requests

def generate_script_with_huggingface(prompt):
    API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-6-llama-30b-xor"
    headers = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 700,
            "do_sample": True
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        return f"❌ Hugging Face API Error: {response.status_code} – {response.text}"
