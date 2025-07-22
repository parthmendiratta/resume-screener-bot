from langchain_openai import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

def get_chain(resume_text: str, jd_text: str) -> ConversationChain:
    """
    Builds and returns a conversation chain with memory.
    Injects resume and job description into the system prompt.
    """
    llm = AzureChatOpenAI( # This is openAI model
        openai_api_key=os.getenv("AZURE_OPENAI_KEY", st.secrets.get("AZURE_OPENAI_KEY", None)),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION", st.secrets.get("AZURE_OPENAI_API_VERSION", None)),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", st.secrets.get("AZURE_OPENAI_ENDPOINT", None)),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT", st.secrets.get("AZURE_OPENAI_DEPLOYMENT", None)),
        model_name=os.getenv("AZURE_OPENAI_MODEL_NAME", "gpt-35-turbo"),
        temperature=0.2
    )

    prompt_prefix = (
        "You are a helpful AI assistant helping a recruiter evaluate resumes.\n"
        "Here is the job description:\n"
        f"{jd_text}\n\n"
        "Here is the candidate's resume:\n"
        f"{resume_text}\n\n"
        "Now answer questions based on both. If something isn't in either, just say you don't know.\n"
    )

    memory = ConversationBufferMemory(memory_key="history", return_messages=True) # this is memory

    conversation = ConversationChain( # this ties the model and memory together
        llm=llm, 
        memory=memory,
        verbose=False,
        input_key="input",
    )

    # Prime the memory with the prompt prefix
    conversation.memory.chat_memory.add_user_message("System initialization")
    conversation.memory.chat_memory.add_ai_message(prompt_prefix)

    return conversation
