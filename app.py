import google.generativeai as genai

# Paste your Gemini API key here
genai.configure(api_key="AQ.Ab8RN6KPd6oGBOAJK50NAMQOVBnujecqsJMBQHqXCkg2lHBJrw")
import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

# Page Config
st.set_page_config(
    page_title="AI Interview Question Generator",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("📌 About")
st.sidebar.info(
    """
    This AI application generates interview questions
    based on job role, skills, and difficulty level.
    """
)

# Main Title
st.title("🤖 AI Interview Question Generator")
st.markdown("---")

# Inputs
job_role = st.text_input("💼 Enter Job Role")

skills = st.text_area(
    "🛠️ Enter Skills (comma separated)"
)

difficulty = st.selectbox(
    "📊 Select Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

# Generate Button
if st.button("🚀 Generate Questions"):

    if not job_role or not skills:
        st.warning("Please enter Job Role and Skills")
    else:

        prompt = f"""
        You are an expert interviewer.

        Generate interview questions for:

        Job Role: {job_role}
        Skills: {skills}
        Difficulty: {difficulty}

        Generate:
        1. 10 Technical Questions
        2. 5 HR Questions

        Format:

        ## Technical Questions

        ## HR Questions
        """

        with st.spinner("Generating Questions..."):

            response = model.generate_content(prompt)

            st.success("Questions Generated Successfully!")

            st.markdown(response.text)