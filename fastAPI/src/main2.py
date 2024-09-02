import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
from app.chatbot.repository.gemini import chat


load_dotenv()

# Setup the page header with streamlit 
st.set_page_config(
    page_title="Jasmine virtual assistant.",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


st.title("🧑‍⚕️ Jasmine virtual doctor")


user_prompt = st.chat_input("Message Jasmine AI...")

if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    response = chat(user_prompt, os.getenv("RAG_CONTEXT"))
    
    with st.chat_message("assistant"):
        st.markdown(response['answer'])