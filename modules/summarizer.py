"""Generates AI-powered compliance and security reports using Gemini API based on detected sensitive data."""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# Main Compliance Summary Generator

def generate_compliance_summary(document_text, detections, risk):
    """
    Generates a structured compliance report.
    """

    # Limit text size for API safety
    document_text = document_text[:12000]

    prompt = f"""
You are a senior cybersecurity and compliance analyst.

Your task is to analyze the document and generate a professional compliance report.

---

DOCUMENT:
{document_text}

---

DETECTED SENSITIVE DATA:
{detections}

---

RISK SCORE:
{risk['score']}

RISK LEVEL:
{risk['level']}

---

Generate a structured report with the following sections:

1. Executive Summary
2. Sensitive Data Identified
3. Compliance Risks (GDPR / DPDP Act / Security Standards)
4. Security Risks
5. Data Exposure Impact
6. Recommended Remediation Steps
7. Final Conclusion

---

Rules:
- Be professional and concise
- Do NOT repeat raw data unnecessarily
- Focus on compliance and security impact
- Use bullet points where needed
"""

    response = model.generate_content(prompt)

    return response.text

# Optional: Quick Risk Insight Generator

def generate_risk_insights(risk):
    """
    Generates quick explanation of risk level.
    """

    prompt = f"""
Explain the following cybersecurity risk level in simple terms:

Risk Score: {risk['score']}
Risk Level: {risk['level']}

Provide:
- What this means
- Why it matters
- What should be done
"""

    response = model.generate_content(prompt)

    return response.text