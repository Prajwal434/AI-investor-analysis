# AI Investor Analysis
# Investor Insights Analyzer

## Overview
The **Investor Insights Analyzer** is a Streamlit-based application that extracts financial insights from investor-related PDFs using Google Gemini AI. The tool helps analyze financial transcripts and provides key investor insights, including sentiment analysis, competitive positioning, and actionable investment recommendations.

## Features
- **PDF Upload Support**: Extracts text from uploaded financial PDFs.
- **AI-Powered Analysis**: Uses Google Gemini AI to summarize key investor insights.
- **Structured Insights**:
  - Future growth prospects
  - Key business changes
  - Market impact triggers
  - Earnings impact analysis
  - Competitive positioning
  - Sentiment analysis (Positive/Neutral/Negative)
  - Actionable investment recommendations (Buy/Hold/Sell)
- **Automatic Report Generation**:
  - Saves insights as `Investor_Summary.txt` and `Investor_Summary.json`.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip (Package Installer for Python)

### Clone the Repository
```sh
git clone https://github.com/your-repo/investor-insights-analyzer.git
cd investor-insights-analyzer
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Google Gemini API Key
1. Create a `.env` file in the root directory.
2. Add your Gemini API key:
   ```sh
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage
### Run the Streamlit App
```sh
streamlit run app.py
```

### Upload & Analyze
1. Upload a **PDF file** containing financial data.
2. Wait for the AI to extract and analyze insights.
3. View the generated insights on the interface.
4. Summary is saved automatically as `Investor_Summary.txt` and `Investor_Summary.json`.

## File Structure
```
├── app.py               # Main application script
├── requirements.txt     # Dependencies
├── .env                 # API key configuration
├── Investor_Summary.txt # Generated text summary (after execution)
├── Investor_Summary.json# JSON summary output (after execution)
```

## Dependencies
- `streamlit`
- `google-generativeai`
- `PyPDF2`
- `python-dotenv`
- `json`
- `os`

## License
This project is licensed under the MIT License.

## Author
[Your Name]

## Contributions
Feel free to contribute! Open an issue or subm