import streamlit as st
from chatbot import get_chain
import PyPDF2
from io import BytesIO

st.set_page_config(page_title="Resume Screener Bot", layout="wide")
st.title("📄 Resume Screener Chatbot")

# --- Utility Function to Extract Text from PDF ---
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# --- Reset Button (outside sidebar) ---
if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.session_state.qa_chain = None
    st.rerun()

# --- Upload Files ---
st.subheader("Upload Resume & Job Description")
resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"], key="resume")
jd_file = st.file_uploader("Upload Job Description PDF", type=["pdf"], key="jd")

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# --- Load and Process PDFs ---
if resume_file and jd_file and st.session_state.qa_chain is None:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)
    st.session_state.qa_chain = get_chain(resume_text, jd_text)
    st.success("✅ Files uploaded and chain initialized. You can start chatting!")

# --- Chat UI Layout ---
chat_container = st.container()
chat_input = st.chat_input("Ask something about the resume or job description...")

# --- Render Chat History ---
with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

# --- Handle New Input ---
if chat_input and st.session_state.qa_chain:
    st.session_state.messages.append({"role": "user", "content": chat_input})
    with st.chat_message("user"):
        st.markdown(chat_input)

    with st.chat_message("assistant"):
        response = st.session_state.qa_chain.run(chat_input)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
