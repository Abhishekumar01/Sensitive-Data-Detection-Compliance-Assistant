"""RAG Chatbot Module
------------------
Creates embeddings using Sentence Transformers,
stores vectors in FAISS,
retrieves relevant document chunks,
and answers user questions using Gemini."""

import os
import numpy as np
import faiss

from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer

# Load Environment Variables

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

genai.configure(api_key=API_KEY)

# Gemini Model

llm = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Embedding Model

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Create Vector Store

def create_vector_store(chunks):
    """
    Creates a FAISS vector index
    from document chunks.
    """

    if not chunks:
        raise ValueError(
            "No document chunks available."
        )

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    embeddings = embeddings.astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, chunks

# Retrieve Context

def retrieve_context(
    question,
    index,
    chunks,
    top_k=4
):
    """
    Retrieves the most relevant chunks
    for the user's question.
    """

    query_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    retrieved_chunks = []

    for idx in indices[0]:

        if idx < len(chunks):

            retrieved_chunks.append(
                chunks[idx]
            )

    return "\n\n".join(
        retrieved_chunks
    )

# Ask Question

def ask_document_question(
    question,
    index,
    chunks
):
    """
    Uses retrieved context
    to answer user questions.
    """

    context = retrieve_context(
        question,
        index,
        chunks
    )

    prompt = f"""
You are an AI Sensitive Data Compliance Assistant.

Your job is to answer ONLY using the provided document context.

If the answer cannot be found in the document,
say:

"I could not find this information in the uploaded document."

------------------------

DOCUMENT CONTEXT

{context}

------------------------

QUESTION

{question}

------------------------

Answer professionally.

If applicable include:

• Sensitive information found

• Compliance risks

• Security concerns

• Recommendations
"""

    response = llm.generate_content(
        prompt
    )

    return response.text

# Quick Summary

def summarize_document(
    index,
    chunks
):
    """
    Generates a concise summary
    of the uploaded document.
    """

    context = retrieve_context(
        "Summarize this document.",
        index,
        chunks,
        top_k=6
    )

    prompt = f"""
Summarize the following document.

Context:

{context}

Return:

1. Purpose

2. Important Information

3. Sensitive Data

4. Compliance Concerns
"""

    response = llm.generate_content(
        prompt
    )

    return response.text