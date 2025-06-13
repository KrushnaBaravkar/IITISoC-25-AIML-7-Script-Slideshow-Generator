import streamlit as st
from llama_agent import script_generator

st.title("🎤 Script & Slideshow Generator")
st.divider()
st.header("📥 Enter Presentation Details")

# Inputs
topic = st.text_input("Topic", placeholder="e.g. Climate Change")
audience = st.selectbox("Select Audience", ["School Students", "College Students", "General Public", "Experts"])
tone = st.selectbox("Select Tone", ["Formal", "Informal", "Inspiring", "Neutral"])
word_count = st.number_input("Desired Length (in words)", min_value=100, max_value=1000, step=50, value=500)

# initialization of session stats.
if 'script' not in st.session_state:
    st.session_state.script = ""
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

# Script generation.
if st.button("🧠 Generate Script"):
    prompt = f"Generate a {tone.lower()} script of about {word_count} words on '{topic}' for {audience.lower()}."
    with st.spinner("LLaMA is generating your script..."):
        result = script_generator(prompt)
        st.session_state.script = result
        st.session_state.edit_mode = False

# Display of script and option to edit if required.
if st.session_state.script:
    st.subheader("📝 Script Output")

    # Edit mode
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

    # Download button
    st.download_button("⬇️ Download Script (.txt)", data=st.session_state.script, file_name="script.txt", mime="text/plain")

    # --- SLIDE PREVIEW & DOWNLOAD ---
    st.subheader("📊 Slide Preview (Placeholder)")
    st.markdown("- Slide 1: Introduction\n- Slide 2: Problem Statement\n- Slide 3: Conclusion")

    st.button("Convert to PPT")
