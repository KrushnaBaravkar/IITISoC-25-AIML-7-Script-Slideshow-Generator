import requests
import json
import ast

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


arr=generate_slide_array(ere is a 500-word script on "Introduction to AI" suitable for college students:
                         

**Title:** Introduction to Artificial Intelligence (AI)

**Slide 1: Introduction**

Good morning/afternoon class, and welcome to our course on Artificial Intelligence. My name is [Your Name], and I will be your instructor for this journey into the world of AI.

Over the past few decades, we have witnessed an exponential growth in technology, leading to incredible advancements in various fields. Among these, Artificial Intelligence has emerged as one of the most promising areas of research and development.

**Slide 2: What is AI?**

So, what exactly is Artificial Intelligence? Simply put, AI refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions.

AI involves a range of disciplines, including computer science, mathematics, engineering, and cognitive psychology. The ultimate goal of AI research is to create intelligent machines that can perform tasks that typically require human intelligence, such as learning, problem-solving, decision-making, and perception.

**Slide 3: Types of AI**

There are several types of AI, each with its unique approach:

1. **Narrow or Weak AI**: Designed to perform a specific task, such as facial recognition, speech recognition, or playing chess.
2. **General or Strong AI**: Aims to create machines that can think and act like humans, possessing common sense and the ability to reason and learn from experience.
3. **Superintelligence**: The hypothetical future state where machines surpass human intelligence in all domains.

**Slide 4: History of AI**

The concept of AI dates back to ancient Greece, but modern AI research began in the mid-20th century with pioneers like Alan Turing, Marvin Minsky, and John McCarthy.

Key milestones include:

1. **Turing Test** (1950): A measure of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.
2. **Rule-based Expert Systems** (1970s): The first AI systems that could reason using rules and heuristics.

**Slide 5: Applications of AI**

AI has numerous applications in various industries, including:

1. **Virtual Assistants**: Siri, Alexa, Google Assistant
2. **Image Recognition**: Self-driving cars, facial recognition, medical diagnosis
3. **Natural Language Processing**: Chatbots, language translation, sentiment analysis
4. **Predictive Analytics**: Customer segmentation, risk assessment, supply chain optimization

**Slide 6: Challenges and Concerns**

As AI becomes more pervasive in our lives, we also face challenges and concerns:

1. **Job Displacement**: The impact of automation on employment.
2. **Bias and Fairness**: Ensuring that AI systems are fair, transparent, and unbiased.
3. **Cybersecurity**: Protecting AI systems from cyber threats and data breaches.

**Slide 7: Conclusion**

In conclusion, Artificial Intelligence is a rapidly evolving field with vast potential benefits and challenges. As we embark on this journey together, I encourage you to explore the many facets of AI and consider its implications for our society.

Over the next few weeks, we will delve deeper into various aspects of AI, including machine learning, deep learning, and natural language processing. Be prepared to engage with real-world examples, case studies, and hands-on activities that will help you understand the inner workings of AI systems.

Thank you for your attention, and let's get started on this exciting journey into the world of Artificial Intelligence!

**Additional Resources:**

* Recommended readings:
 + "Artificial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig
 + "Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville
* Online resources:
 + AI courses on Coursera, edX, or Udemy
 + Research papers and articles on arXiv, Nature, or Science)

print("arr:", arr)
print("type(arr[0]):", type(arr[0]))

