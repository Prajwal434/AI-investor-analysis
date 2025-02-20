import streamlit as st
import google.generativeai as genai
import PyPDF2
import json
import os
from dotenv import load_dotenv



# Load API Key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if GOOGLE_API_KEY is None:
    st.error("🚨 Error: GEMINI_API_KEY is not found. Check your .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

def extract_text_from_pdf(pdf_file):
    """Extracts text from a given PDF file."""
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text + "\n"
    return text

def analyze_text_with_gemini(text):
    """Uses Gemini API to analyze and summarize investor insights."""
    prompt = f"""
    Analyze the following financial transcript and extract **detailed investor insights**.

    ### Key Areas:
    1. **Future Growth Prospects** – Expansion plans, market positioning.
    2. **Key Changes in the Business** – Mergers, acquisitions, leadership shifts.
    3. **Key Triggers** – Major catalysts impacting valuation.
    4. **Material Impact on Earnings** – Revenue drivers, cost implications.
    5. **Competitive Position** – Strengths vs. competitors.
    6. **Sentiment Analysis** – Is the outlook **positive, neutral, or negative**?
    7. **Actionable Investment Insights** – Buy, hold, or sell recommendation?

    **Output structured in bullet points. Keep it concise but insightful.**

    **Financial Transcript:**
    {text}
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text.strip()

# Streamlit UI
st.title("📊 Investor Insights Analyzer")
st.write("Upload a **PDF** to extract and analyze key financial insights.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")
    
    with st.spinner("Extracting text..."):
        pdf_text = extract_text_from_pdf(uploaded_file)
    
    with st.spinner("Analyzing with Gemini AI..."):
        summary = analyze_text_with_gemini(pdf_text)

    st.subheader("📌 Investor Insights Summary")
    st.write(summary)

    # Save results
    with open("Investor_Summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    summary_data = {"summary": summary}
    with open("Investor_Summary.json", "w", encoding="utf-8") as file:
        json.dump(summary_data, file, indent=4)

    st.success("✅ Summary saved as 'Investor_Summary.txt' and 'Investor_Summary.json'!")
