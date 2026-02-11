import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_matcher import calculate_match, missing_skills

st.title("🚀 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:

    resume_text = extract_text_from_pdf(uploaded_file)

    score = calculate_match(resume_text, job_description)

    st.success(f"✅ Match Score: {score}%")

    if score > 75:
        st.write("🔥 Excellent match! You are job ready.")
    elif score > 50:
        st.write("👍 Good match but can improve.")
    else:
        st.write("⚠️ Low match. Add more relevant skills.")

    skills = missing_skills(resume_text, job_description)

    st.subheader("📌 Suggested Skills to Add:")
    st.write(skills)
