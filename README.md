# AI Lawyer Chatbot RAG

This project is an AI-powered private document chatbot using Retrieval-Augmented Generation (RAG) and FAISS vector database. Users can upload PDF documents and ask questions related to the content.
![Uploading image.png…]()

## Features

- Upload PDF documents
- Ask questions about uploaded documents
- Uses RAG pipeline for document retrieval and LLM for answering
- Streamlit-based web interface

## Project Structure

```
fronend.py                # Streamlit UI for chatbot
RAG_Pipeline.py           # RAG pipeline logic (retriever, LLM, memory)
vector_database.py        # PDF upload and vector database management
pdfs/                     # Uploaded PDF files
vectorstore/db_faiss/     # FAISS vector index and metadata
```

## Getting Started

1. **Install dependencies**  
   Make sure you have Python 3.12+ and install required packages:
   ```sh
   pip install streamlit
   # Add other dependencies as needed
   ```

2. **Run the app**
   ```sh
   streamlit run fronend.py
   ```

3. **Usage**
   - Upload a PDF file using the UI.
   - Enter your question in the text area.
   - Click "Ask anything related to documents" to get an answer.

## Files

- [fronend.py](fronend.py): Streamlit UI
- [RAG_Pipeline.py](RAG_Pipeline.py): RAG pipeline functions ([`answer_query`](RAG_Pipeline.py), [`retriver_docs`](RAG_Pipeline.py), [`llm_model`](RAG_Pipeline.py), [`memory`](RAG_Pipeline.py))
- [vector_database.py](vector_database.py): PDF upload ([`uplaod_pdf`](vector_database.py))
