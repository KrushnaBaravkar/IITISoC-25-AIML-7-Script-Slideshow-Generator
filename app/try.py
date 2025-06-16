import requests
import json
import ast

def generate_slide_array(script):
    url = "http://localhost:11434/api/chat"

    # Stricter prompt to ensure model only returns 2D array
    prompt = f"""
You are a helpful assistant that converts a lecture or educational script into slide content.

Your task is to:
- Extract exactly 9 slides.
- Each slide must be a list of two items: [slide title, slide body].
- Return all 9 slides as a JSON array (2D array).
- No preamble, explanation, markdown, or formatting — just raw JSON.
- Keep titles short (3–6 words) and body content in 1–2 bullet points or 1 paragraph.
- DO NOT write anything else except the JSON array.

SCRIPT:
{script}

Now return the 9-slide array in JSON format only:
"""

    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            raw_content = data.get("message", {}).get("content", "")

            print("⚠️ RAW RESPONSE:\n", raw_content)  # Optional: debug the actual response

            # Try parsing as JSON directly
            if raw_content.strip().startswith("[") and raw_content.strip().endswith("]"):
                return json.loads(raw_content)

            # Fallback: try evaluating it as Python literal
            return ast.literal_eval(raw_content)

        else:
            return f"Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"Exception occurred: {e}"


# Example usage
if __name__ == "__main__":
    with open("script.txt", "r", encoding="utf-8") as f:
        script_text = f.read()

    slide_array = generate_slide_array(script_text)
    print("\n✅ Parsed Slide Array:")
    print(slide_array)
