import requests
import json

def script_generator(prompt):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.2",  # Or "llama3.2" if that's your model name
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False  # Disable streaming for simplicity
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data["message"]["content"]
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {e}"

