# Script & Slideshow Generator

🚀 A user-friendly AI tool that generates structured educational scripts and slideshows using open-source NLP models like T5 or GPT-J.

## Features
- 📜 Generate scripts based on topic, audience, tone
- 🧠 Powered by Hugging Face Transformers
- 🖼 Converts content to PowerPoint slides
- 🎛 Interactive UI with Streamlit.

## Demo
_Add screenshots or a short GIF/video here_

## Setup

```bash
git clone https://github.com/aryan6336/IITISoC-25-AIML-7-Script-Slideshow-Generator.git
cd Script-Slideshow-Generator
pip install -r requirements.txt
streamlit run app/ui.py
```

## TimeLine

### Week-1
Working on user interface(UI).
- want to creat WEB-APPLICATION to represent our model for fesable use.
- following is the application overview which will be created using streamlit.
- why streamlit?
  - more easier to build than other methods.
  - includes only python.
  - mostly working with python developers.
  - mostly used in data-science/ML field.
- Application Workflow:
1.User Input & Button Creation:
  -The application takes user input and creates a button.
  -When clicked, the button passes the input to a script generator.

2.Script Generation Process:
  -While the script is being generated, the application displays a loading symbol (e.g., a spinning animation).
  -Once the script is ready, it shows two options:
     -Extract Script
     -Create PPT

3.PPT Generation:
  -If the user selects "Create PPT", the script is sent to PowerPoint (PPTX) to generate the presentation.
  -During this process, the application shows a loading indicator.

4.PPT Display & Options:
  -Once the PPT is ready, the application displays the generated presentation.
  -It provides two options at the bottom:
     -Export
     -Edit

5.Editing Functionality:
  -If the user clicks "Edit", they can modify the text in the PowerPoint.

- 

## 👤 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/aryan-kumar-222b1531a/)

