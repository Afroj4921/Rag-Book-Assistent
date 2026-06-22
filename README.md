# Rag-Book-Assistent

# 📚 RAG Book Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content using Mistral AI, LangChain, and ChromaDB.

## 🚀 Features

* Upload PDF documents
* Automatic text extraction and chunking
* Generate vector embeddings using Mistral AI
* Store embeddings in ChromaDB
* Semantic search with MMR retrieval
* Context-aware question answering
* Interactive Streamlit interface

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* ChromaDB
* PyPDF
* Vector Embeddings
* Retrieval-Augmented Generation (RAG)

## 📂 Project Structure

```text
RAG-Book-Assistant/
│
├── app.py
├── main.py
├── create_database.py
├── requirements.txt
├── .gitignore

│# these forlders are only for educational perpose only and do not have any contribution to the project
├── document loaders/
├── retrivers/
└── vector_store/
```

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Afroj4921/Rag-Book-Assistent.git
cd Rag-Book-Assistent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

## ▶️ Running the Application

### Create Vector Database

```bash
python create_database.py
```

### Launch Streamlit App

```bash
streamlit run app.py
```

## 💡 How It Works

1. Upload a PDF document.
2. Text is extracted and split into chunks.
3. Mistral AI generates embeddings for each chunk.
4. ChromaDB stores and retrieves relevant information.
5. The LLM answers questions using only the retrieved context.

## 🎯 Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Prompt Engineering
* Large Language Model Integration
* Document Question Answering Systems

## 📌 Future Improvements

* Multi-PDF support
* Chat history memory
* Source citations
* Hybrid search
* Cloud deployment

## 👨‍💻 Author

**Afroj Ansari**

B.Tech CSE Student | AI/ML Enthusiast | Generative AI Learner

GitHub: https://github.com/Afroj4921
