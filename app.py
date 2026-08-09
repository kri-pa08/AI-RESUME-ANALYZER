import streamlit as st
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="ResumeIQ | AI Resume Analyzer",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: #f7f8fc;
    }

    /* Remove default top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 1200px;
    }

    /* Header */
    .brand {
        font-size: 32px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 0;
    }

    .brand span {
        color: #635bff;
    }

    .tagline {
        color: #6b7280;
        font-size: 16px;
        margin-top: 5px;
        margin-bottom: 30px;
    }

    /* Cards */
    .card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 5px;
    }

    .card-subtitle {
        color: #6b7280;
        font-size: 13px;
        margin-bottom: 15px;
    }

    /* Score */
    .score-card {
        background: white;
        border-radius: 18px;
        padding: 28px;
        text-align: center;
        border: 1px solid #e5e7eb;
        box-shadow: 0 5px 18px rgba(0,0,0,0.05);
    }

    .score {
        font-size: 48px;
        font-weight: 800;
        color: #635bff;
    }

    .score-label {
        color: #6b7280;
        font-size: 14px;
    }

    /* Skill pills */
    .skill {
        display: inline-block;
        padding: 7px 12px;
        margin: 4px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    .matched {
        background: #ecfdf5;
        color: #047857;
    }

    .missing {
        background: #fff7ed;
        color: #c2410c;
    }

    /* Divider */
    .divider {
        height: 1px;
        background: #e5e7eb;
        margin: 30px 0;
    }

    /* Analyze button */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 48px;
        font-size: 16px;
        font-weight: 700;
        background: #635bff;
        color: white;
        border: none;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background: #5148e5;
        color: white;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background: #fafaff;
        border-radius: 12px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="brand">◈ Resume<span>IQ</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">'
    'AI-powered resume intelligence • Match your profile with the right role'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- INPUT SECTION ----------------

col1, col2 = st.columns(2, gap="large")


with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">📄 Upload Resume</div>
        <div class="card-subtitle">
            Upload your resume in PDF format
        </div>
    """, unsafe_allow_html=True)

    resume = st.file_uploader(
        "Choose PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">💼 Job Description</div>
        <div class="card-subtitle">
            Paste the job description you are applying for
        </div>
    """, unsafe_allow_html=True)

    job_description = st.text_area(
        "Job Description",
        height=170,
        placeholder="Paste the complete job description here...",
        label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- RESUME EXTRACTION ----------------

resume_text = ""

if resume:

    resume_text = extract_text_from_pdf(resume)

    with st.expander("View extracted resume text"):

        st.text_area(
            "Resume Content",
            resume_text,
            height=250,
            label_visibility="collapsed"
        )


# ---------------- ANALYZE ----------------

st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button("✦  Analyze Resume")


if analyze:

    if not resume:

        st.warning("Please upload your resume first.")

    elif not job_description.strip():

        st.warning("Please paste the job description first.")

    else:

        with st.spinner("Analyzing your profile..."):

            try:

                result = analyze_resume(
                    resume_text,
                    job_description
                )

                st.markdown(
                    '<div class="divider"></div>',
                    unsafe_allow_html=True
                )

                st.markdown("## 📊 Resume Analysis")

                st.markdown(
                    '<div class="card">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    result
                )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# ---------------- FOOTER ----------------

st.markdown(
    "<br><br><center style='color:#9ca3af;font-size:12px;'>"
    "ResumeIQ • AI Resume Intelligence"
    "</center>",
    unsafe_allow_html=True
)