# 📄 Resume Screener Bot – RAG Chatbot with LangChain, Streamlit & Azure OpenAI

A modern AI-powered resume screener bot that allows HRs and recruiters to **upload resumes and job descriptions**, then **ask questions** or get insights using **LangChain**, **FAISS**, and **Azure OpenAI (GPT-3.5 Turbo)** — all through a polished **Streamlit chat UI**.

---

## 🚀 Features

- 🧠 **RAG pipeline** powered by LangChain + FAISS + Azure OpenAI
- 📝 Upload **resume** and **job description** PDFs directly via Streamlit
- 💬 Clean, chat-style interface with real-time Q&A
- 🔄 “Reset” button to upload new docs and restart chat
- 🎨 Frontend UI styled like a messaging app

---

## 🗂️ Project Structure

```
resume-screener-bot/
│
├── chatbot.py               # All core logic for embedding + RAG chain
├── app.py                   # Streamlit UI and chat frontend
├── requirements.txt         # All required Python packages
├── .gitignore
├── README.md
└── .streamlit/
    └── secrets.toml         # Your Azure OpenAI credentials (never upload)
```

---

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

> ⚠️ Keep your secrets.toml safe and private. It's ignored by `.gitignore`.

---

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

Then go to `http://localhost:8501` in your browser.

---

## 🧠 How It Works

1. User uploads a **resume** and **job description** (PDFs).
2. The PDFs are split into chunks and embedded using `AzureOpenAIEmbeddings`.
3. FAISS is used to create a vector store for similarity search.
4. When the user sends a message, the top-matching chunks are retrieved.
5. These are passed along with the question to a GPT model via LangChain's `RetrievalQA`.

---

## 🖼️ Screenshot

> _(Add screenshot here of chat interface for visual appeal)_

---

## 🌍 Deploy on Streamlit Cloud (Optional)

Once deployed, update this link:

🔗 [Live Demo](https://resume-screener-bot-yourusername.streamlit.app)

---

## 🙌 Author

Made with ❤️ by [Parth Mendiratta](https://github.com/parthmendiratta)

---

## ⭐ Like This Project?

If this helped you, consider starring ⭐ the repository and sharing it!
