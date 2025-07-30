
# 📚 Script & Slideshow Generator

A powerful, user-friendly AI tool that automatically generates educational **scripts** and corresponding **PowerPoint presentations** based on your input. Built with **Streamlit** for an intuitive interface, and powered by open-source large language models like **LLaMA 3.2**, this project is perfect for educators, students, and content creators.

---

## 🔧 Features

- 🎯 **Topic-Based Script Generation**: Generate educational scripts based on topic, tone, and target audience.
- 🤖 **Powered by Local LLaMA 3.2**: Efficient and private inference using `Ollama` and `transformers`.
- 🧠 **Intelligent Slide Structuring**: Automatically splits the script into slide-sized chunks with title and content.
- 📊 **PowerPoint Export**: Export slides as `.pptx` and optionally as `.pdf`.
- 🛠 **Interactive UI**: Built with **Streamlit**, requiring no coding knowledge to use.
- 📝 **Editable Presentations**: Users can modify the content before exporting.

---

## 🖥 Demo

[![Watch the video](https://img.youtube.com/vi/MNnjGcmR7SM/hqdefault.jpg)](https://www.youtube.com/watch?v=MNnjGcmR7SM)

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+
- Install [Ollama](https://ollama.com/) to run LLaMA 3.2 locally
- PowerPoint (optional, for viewing `.pptx` files)

### 📦 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/aryan6336/IITISoC-25-AIML-7-Script-Slideshow-Generator.git
cd IITISoC-25-AIML-7-Script-Slideshow-Generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the Streamlit app:
```bash
streamlit run app/ui.py
```

---

## 📁 Project Structure

```bash
├── app/
│   ├── ui.py               # Streamlit user interface
│   ├── llama_agent.py      # LLaMA3-based script & slide generation
│   ├── slide_maker.py      # PPTX file generation & export logic
│   └── templates/          # PPT templates for slide formatting
├── powerpoints/            # Output folder for generated presentations
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---


### Application Workflow:

1. **Input & Generation**
   - User enters the topic, audience, and tone.
   - Click “Generate Script” to invoke the LLaMA model via Ollama.

2. **Script Output**
   - After processing, the script appears in editable format.
   - Users can preview or edit the content.

3. **Slide Creation**
   - On clicking “Create Slides”, the script is automatically structured into slides (title + content).
   - Template-specific layout logic is applied.

4. **Export Options**
   - Users can choose to download the presentation as a `.pptx` or `.pdf`.

5. **Live Editing**
   - Each slide's content can be manually edited before exporting.

---

## 🧠 Technologies Used

| Technology        | Purpose                                  |
|-------------------|------------------------------------------|
| Python            | Core language                            |
| Streamlit         | UI development                           |
| Ollama + LLaMA 3.2| Local LLM inference                      |
| python-pptx       | PowerPoint automation                    |
| LangChain         | LLM orchestration (optional backend)     |

---

## ❗ Notes

- This tool is designed for **local** use to ensure privacy and low latency.
- You must have `Ollama` running with a locally available `llama3` model (3.2B or higher) for inference to work.

---

## 🙋‍♂️ Author

**Aryan Kumar**

- 👨‍🎓 B.Tech - Mechanical Engineering, IIT Indore
- 💡 Interested in AI, robotics, automation, and system design

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/aryan-kumar-222b1531a/)

**Krushna baravkar**

- 👨‍🎓 B.Tech - Mechanical Engineering, IIT Indore
- 💡 Interested in AI and ML, robotics.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/krushna-baravkar-182299353/)

---

## 📃 License

This project is open-sourced under the [MIT License](LICENSE).
