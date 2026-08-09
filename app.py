import streamlit as st
from resume_parser import extract_text_from_pdf


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume to extract and analyze its content."
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if resume:
    resume_text = extract_text_from_pdf(resume)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    ) 
    st.subheader("Job Description")

job_description = st.text_area(
    "Paste the Job Description here",
    height=250,
    placeholder="Paste the job description here..."
)
if st.button("Analyze Resume"):
    if not resume:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter the job description.")

    else:
        st.success("Resume and Job Description received!")