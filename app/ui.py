import streamlit as st
import base64
import os

from llama_agent import script_generator, generate_slide_array
from slide_maker import slide_generation_1, slide_generation_2

st.title("🎤 Script & Slideshow Generator")
st.divider()
st.header("📥 Enter Presentation Details")

# Inputs
topic = st.text_input("Topic", placeholder="e.g. Climate Change")
audience = st.selectbox("Select Audience", ["School Students", "College Students", "General Public", "Experts"])
tone = st.selectbox("Select Tone", ["Formal", "Informal", "Inspiring", "Neutral"])
word_count = st.number_input("Desired Length (in words)", min_value=100, max_value=1000, step=50, value=500)

# Template selection with preview
st.subheader("🧰 Choose Slide Template")
template_dict = {
    "Template 1": "template1",
    "Template 2": "template2",
    "Template 3": "template3"
}

cols = st.columns(3)
for idx, (label, value) in enumerate(template_dict.items()):
    with cols[idx]:
        st.image(f"assets/{value}.jpg", caption=label, use_column_width=True)

template_selection = st.radio("Select a Template:", list(template_dict.keys()), horizontal=True)
template_type = template_dict[template_selection]

# State init
if 'script' not in st.session_state:
    st.session_state.script = ""
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False
if 'ppt_generated' not in st.session_state:
    st.session_state.ppt_generated = False

# Script generation
if st.button("🧠 Generate Script"):
    prompt = f"Generate a {tone.lower()} script of about {word_count} words on '{topic}' for {audience.lower()}."
    with st.spinner("LLaMA is generating your script..."):
        result = script_generator(prompt)
        st.session_state.script = result
        st.session_state.edit_mode = False
        st.session_state.ppt_generated = False

# Display script
if st.session_state.script:
    st.subheader("📝 Script Output")

    if st.session_state.edit_mode:
        edited_script = st.text_area("Edit your script", value=st.session_state.script, height=250, key="edit_area")
        if st.button("💾 Save Changes"):
            st.session_state.script = edited_script
            st.session_state.edit_mode = False
            st.success("✅ Script updated!")
    else:
        st.text_area("Script", value=st.session_state.script, height=250, disabled=True)
        if st.button("✏️ Edit Script"):
            st.session_state.edit_mode = True

    st.download_button("⬇️ Download Script (.txt)", data=st.session_state.script, file_name="script.txt", mime="text/plain")

    # SLIDES
    st.subheader("📊 Slide Generator")
    if st.button("🧩 Convert to Slides"):
        with st.spinner("Creating slides from script..."):
            arr = generate_slide_array(st.session_state.script)
            if template_type=="template1" or template_type=="template3":
                slide_generation_1(arr, template_type)
            else:
                slide_generation_2(arr,template_type)
            st.session_state.ppt_generated = True
            st.success("✅ Slides generated successfully!")

    if st.session_state.ppt_generated:
        pptx_path = "powerpoints/generated_presentation.pptx"
        if os.path.exists(pptx_path):
            with open(pptx_path, "rb") as f:
                pptx_bytes = f.read()
            st.download_button("⬇️ Download Slides (.pptx)", data=pptx_bytes, file_name="slides.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")

