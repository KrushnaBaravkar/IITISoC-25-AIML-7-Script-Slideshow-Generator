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
Given the following script, extract exactly 9 slides. Each slide should be represented as a list of two elements:

["Slide Title", "Slide Body Content"]

Follow this format and output a 2D JSON array containing 9 items, one for each slide.
Avoid introductory comments or formatting. Output only valid JSON.

SCRIPT:
{script}

Now generate the 9-slide array:
"""

    payload = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            raw = data["message"]["content"].strip()

            # Try JSON parsing
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError:
                parsed = ast.literal_eval(raw)

            # Validate structure
            if (
                isinstance(parsed, list) and
                len(parsed) == 9 and
                all(isinstance(slide, list) and len(slide) == 2 for slide in parsed)
            ):
                return parsed
            else:
                raise ValueError("Response structure is not a 2D array of 9 [title, content] pairs.")

        else:
            raise RuntimeError(f"Ollama API Error {response.status_code}: {response.text}")

    except Exception as e:
        print("❌ Unexpected structure returned from LLM:")
        print(e)
        return [["Error", "Failed to generate slide content. Please try again."]] * 9


