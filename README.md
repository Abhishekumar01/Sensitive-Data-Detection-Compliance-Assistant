🔒 Sensitive Data Detection & Compliance Assistant

📌 Project Overview

The Sensitive Data Detection & Compliance Assistant is an AI-powered document analysis system that detects Personally Identifiable Information (PII) and confidential business data from uploaded documents. It classifies risk levels, generates compliance reports using Generative AI, and allows users to interact with documents using a RAG-based chatbot.

This system is designed for data privacy, cybersecurity compliance, and enterprise document governance.

🚀 Setup Instructions

1. Clone the Repository
git clone https://github.com/your-username/sensitive-data-compliance-assistant.git
cd sensitive-data-compliance-assistant

2. Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Add Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here

5. Run the Application

streamlit run app.py

🧠 Architecture Overview

System Architecture Flow
                ┌──────────────────────┐
                │   User Upload File   │
                └─────────┬────────────┘
                          │
          ┌───────────────▼────────────────┐
          │ PDF / TXT / CSV Text Extractor │
          └───────────────┬────────────────┘
                          │
        ┌─────────────────▼──────────────────┐
        │ Sensitive Data Detection (Regex)   │
        └─────────────────┬──────────────────┘
                          │
        ┌─────────────────▼──────────────────┐
        │ Risk Scoring Engine (Weighted)     │
        └─────────────────┬──────────────────┘
                          │
        ┌─────────────────▼──────────────────┐
        │ AI Compliance Summary (Gemini AI)  │
        └─────────────────┬──────────────────┘
                          │
        ┌─────────────────▼──────────────────┐
        │ Data Masking / Redaction Layer     │
        └─────────────────┬──────────────────┘
                          │
        ┌─────────────────▼──────────────────┐
        │ RAG Chatbot (FAISS + Embeddings)   │
        └─────────────────────────────────────┘
Key Components
Frontend: Streamlit UI
Backend: Python
AI Engine: Google Gemini API
Vector Search: FAISS
Embeddings: Sentence Transformers
Text Processing: LangChain
Detection Engine: Regex + rule-based NLP

🧠 AI/ML Approach Used

1. Sensitive Data Detection (Rule-Based NLP)
Uses regular expressions (Regex) to detect:
Aadhaar numbers
PAN numbers
Emails
Phone numbers
Credit cards
API keys
Passwords

2. Risk Classification (Rule-Based ML Logic)

A weighted scoring system assigns risk values:

Data Type	Weight
Email	        2
Phone	        2
PAN	        5
Aadhaar	        5
Credit Card	8
API Key	        10
Password	10

Final classification:

| Score | Level |
|-------|--------|
| 0–9 | 🟢 Low |
| 10–24 | 🟡 Medium |
| 25+ | 🔴 High |

3. Embedding-Based Retrieval (RAG)
Uses Sentence Transformers (all-MiniLM-L6-v2)
Converts document into vector chunks
Stores embeddings in FAISS index
Retrieves top-k relevant chunks

4. Generative AI (LLM)
Uses Google Gemini API
Generates:
Compliance reports
Security insights
Risk explanations
Remediation steps

5. Retrieval-Augmented Generation (RAG)

Pipeline:

User Query → Embedding → FAISS Search → Context Retrieval → Gemini Answer

⚠️ Challenges Faced

1. Multi-format Document Handling
Handling PDF, TXT, and CSV extraction consistently was challenging.

2. Regex Accuracy
Avoiding false positives (especially for credit cards and bank numbers).

3. Vector Search Optimization
Balancing chunk size for FAISS retrieval accuracy.

4. LLM Prompt Engineering
Ensuring Gemini generates structured compliance reports.

5. Streamlit State Management
Maintaining chat history across interactions.

6. Performance Optimization
Embedding large documents efficiently without freezing UI.

🚀 Future Improvements:

🔐 OCR support for scanned PDFs and images
🧾 PDF compliance report export (professional PDF output)
🐳 Docker containerization
☁️ AWS / Azure deployment
👥 Multi-user authentication system
📊 Advanced analytics dashboard
🔐 Encryption for sensitive data storage
📁 Database integration (PostgreSQL / MongoDB)
🧠 Fine-tuned domain-specific LLM for compliance
🌐 Working Prototype Deployment Link (MANDATORY)

👉 Replace this with your actual deployed link after hosting:

https://your-app-name.streamlit.app

👨‍💻 Author
Abhishek Kumar
AI Engineer | Data Scientist | Machine Learning Enthusiast

GitHub:
https://github.com/Abhishekumar01

LinkedIn:
www.linkedin.com/in/abhishekkumar6360

Built using Python, Streamlit, Gemini AI, FAISS, and NLP techniques.

⭐ Summary

This project demonstrates a full-stack AI system combining:
NLP-based sensitive data detection
Risk scoring system
Generative AI compliance reporting
RAG-based document Q&A
Enterprise-level UI dashboard

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---