import streamlit as st
from utils import (
    extract_text_from_pdf,
    extract_skills_from_resume,
    get_skill_recommendations,
    get_career_advice,
    plot_skill_chart
)

st.set_page_config(page_title="GenAI Career Navigator", layout="wide")
st.title("🧭 GenAI Career Navigator")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
if uploaded_file:
    # Get resume text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Extract skills
    st.subheader("🔍 Extracted Skills")
    extracted_skills = extract_skills_from_resume(resume_text)
    st.write(", ".join(extracted_skills) if extracted_skills else "No obvious skills detected.")

    # Skill recommendations
    st.subheader("✨ GenAI Skill Recommendations")
    recommended = get_skill_recommendations(extracted_skills)
    st.write("• " + "\n• ".join(recommended) if recommended else "No recommendations available.")

    # Career advice (optional input)
    st.subheader("🧠 Ask GPT for Career Advice")
    question = st.text_input("Ask anything about your GenAI career (e.g., 'What roles fit my skills?')")
    if question:
        response = get_career_advice(resume_text, question)
        st.write(response)

    # Skill chart
    st.subheader("📊 Career Skill Chart")
    fig = plot_skill_chart(extracted_skills, recommended)
    st.pyplot(fig)
