import streamlit as st
import PyPDF2
from openai import OpenAI

# OpenAI API Key
client = OpenAI(api_key="PASTE_YOUR_API_KEY_HERE")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume PDF", type="pdf")

if uploaded_file:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Resume Text")
    st.write(text)

    if st.button("Analyze Resume"):

        prompt = f"""
        Analyze this resume and provide:
        1. ATS Score
        2. Strengths
        3. Missing Skills
        4. Suggestions for Improvement

        Resume:
        {text}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content

        st.subheader("Analysis Result")
        st.write(result)
