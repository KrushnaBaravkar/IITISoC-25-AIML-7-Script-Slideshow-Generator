import streamlit as st
from llama_agent import generate_script_with_huggingface

st.title("🎤 Script & Slideshow Generator")
st.divider()
st.header("📥 Enter Presentation Details")

# Inputs
topic = st.text_input("Topic", placeholder="e.g. Climate Change")
audience = st.selectbox("Select Audience", ["School Students", "College Students", "General Public", "Experts"])
tone = st.selectbox("Select Tone", ["Formal", "Informal", "Inspiring", "Neutral"])
word_count = st.number_input("Desired Length (in words)", min_value=100, max_value=2000, step=50, value=500)

# Prompt preview
st.divider()
if st.button("🧠 Generate Prompt"):
    prompt = f"Generate a {tone.lower()} script of about {word_count} words for a presentation on '{topic}' for {audience.lower()}."
    st.subheader("📜 Formatted Prompt")
    st.write(prompt)
    
    with st.spinner("LLaMA is generating your script..."):
        result =generate_script_with_huggingface(prompt)  # 🔥 Calling your API function

    # Simulated Output
    st.subheader("📝 Script Output (Placeholder)")
    st.text_area("Script", value=result, height=250)

    st.subheader("📊 Slide Preview (Placeholder)")
    st.markdown("- Slide 1: Introduction\n- Slide 2: Problem Statement\n- Slide 3: Conclusion")

    # Download Buttons (Simulated)
    st.download_button("⬇️ Download Script (.txt)", data="Your generated script...", file_name="script.txt")
    st.download_button("⬇️ Download Slides (.pptx)", data=b"FAKEPPTDATA", file_name="slides.pptx")
