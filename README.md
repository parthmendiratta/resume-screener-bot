# 📄 Resume Screener Bot – RAG Chatbot with LangChain, Streamlit & Azure OpenAI

A modern AI-powered resume screener bot that allows HRs and recruiters to **upload resumes and job descriptions**, then **ask questions** or get insights using **LangChain**, **FAISS**, and **Azure OpenAI (GPT-3.5 Turbo)** — all through a polished **Streamlit chat UI**.

## 🚀 Features

- 🧠 RAG pipeline powered by LangChain + FAISS + Azure OpenAI
- 📄 Upload Resume and Job Description PDFs directly in the Streamlit interface
- 💬 Conversational chat interface styled like a real messaging app
- 🔄 "Reset" button to clear docs and start fresh
- 📌 Chat memory support across multiple questions

## 🗂️ Project Structure

```
resume-screener-bot/
│
├── app.py                  # Streamlit UI & frontend logic
├── chatbot.py              # Embedding, RAG chain, and PDF parsing
├── requirements.txt        # Python dependencies
├── .gitignore
├── README.md
└── .streamlit/
    └── secrets.toml        # Azure OpenAI credentials (ignored by Git)
```

## 🔧 Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/parthmendiratta/resume-screener-bot.git
cd resume-screener-bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Azure OpenAI Credentials

Create a file at `.streamlit/secrets.toml` and add:

```toml
[azure]
openai_api_key = "your-azure-openai-key"
openai_api_base = "https://your-resource-name.openai.azure.com/"
openai_api_version = "2025-01-01-preview"
deployment_name = "gpt-35-turbo"
```

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

Then go to `http://localhost:8501` in your browser.

## 🧠 How It Works

1. User uploads a resume and a job description (PDF).
2. Text is extracted and chunked from both files.
3. Embeddings are generated using `AzureOpenAIEmbeddings`.
4. A FAISS vector store is built to store and search the documents.
5. When the user sends a query:
   - Top relevant chunks are retrieved via similarity search.
   - These chunks + the user query are passed to Azure OpenAI via LangChain's `RetrievalQA`.
   - The chatbot returns a contextual, accurate response.

## 🖼️ Screenshots

> Add a screenshot of the chatbot UI here (optional)

## 🌍 Live Demo

🔗 [Try It Here](https://resume-screener-bot-xcrhhzqkvkmawpqgdql4eo-parthmendiratta.streamlit.app/)

## 🙌 Author

Made with ❤️ by [Parth Mendiratta](https://github.com/parthmendiratta)

## ⭐ Like This Project?

If this helped you, consider starring ⭐ the repo and sharing it with others!
