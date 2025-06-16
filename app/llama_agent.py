import requests
import json
import ast

# Call LLM to generate a script based on a prompt
def script_generator(prompt):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.2",  # Adjust to your local model name if needed
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
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

# Call LLM to convert a script into a 9-slide array (2D list)
def generate_slide_array(script):
    url = "http://localhost:11434/api/chat"

    prompt = f"""
You are a helpful assistant that converts lecture or presentation scripts into slide content.
Given the following script, extract exactly 9 slides. Each slide should be represented as an array of two elements:

["Slide Title", "Slide Body Content"]

Follow this format and output a 2D JSON array containing 9 items, one for each slide. Keep the title concise (3–6 words) and the content brief and informative (1–3 bullet points or 1 paragraph max). Avoid including slide numbers or extra formatting. Do not write an introduction or explanation.

SCRIPT:
{script}

Now generate the 9-slide array:
"""

    payload = {
        "model": "llama3.2",  # Adjust to your model name
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            raw_content = data["message"]["content"]
            try:
                return json.loads(raw_content)
            except json.JSONDecodeError:
                return ast.literal_eval(raw_content)
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {e}"
