# 🧠 RAG Assistant - Document Query System

A Retrieval-Augmented Generation (RAG) prototype that enables intelligent question-answering over custom documents using **LangChain**, **Pinecone**, and **OpenAI Embeddings**.  
Built with a **FastAPI backend** and a **Streamlit frontend**.

---

## 🚀 Features

- 📄 Document ingestion, splitting, and embedding using OpenAI
- 📦 Vector storage and retrieval with Pinecone
- 🧠 Context-aware responses powered by LLM (GPT)
- 🔍 Semantic similarity search for accurate context
- 💬 Interactive UI built with Streamlit

---


## ⚙️ Workflow Overview

```plaintext
User Query → Retrieve relevant docs from Pinecone → Combine with context →
LLM (OpenAI GPT) generates final answer → Response displayed on Streamlit
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Sameera626/rag-assistant.git
cd rag-assistant
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file inside the project root:

```env
OPENAI_API_KEY=your_openai_api_key
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=language model
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX=your pinecone index
```

---

## 🧹 Running the Project

### Start Backend (FastAPI)
```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend (Streamlit)
```bash
streamlit run streamlit_app.py
```

---

## 🗃️ Embedding Documents

To embed and upsert documents into Pinecone, run:
```bash
python ingest.py
```

---


## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| Vector DB | Pinecone |
| LLM | OpenAI GPT-4o-mini |
| Framework | LangChain |
| Backend | FastAPI |
| Frontend | Streamlit |
| Embedding | OpenAI Embeddings |
| Language | Python |

---


## 📈 Future Improvements

- Add document upload via Streamlit UI  
- Integrate FAISS as alternative vector store  
- Deploy backend on Render and Streamlit UI on Vercel

---

## 📜 License

MIT License © 2025 [Sameera Athukorala]

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome!  
Please open an issue or a pull request.

---

