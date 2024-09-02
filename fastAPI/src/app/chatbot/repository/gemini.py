from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from app.chatbot.helper.pdf_loader import get_document as pdf_loader
from app.chatbot.helper.googleembeddings import get_retriever
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()
GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")

def chat(user_prompt, context, history: bool = False):
    gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", 
                                    temprature=0, 
                                    max_tokens=200)
    
    prompt_template = ("""
                You are AI powered chatbot designed to provide 
                information and assistance for customers based on the context
                provided to you only. Do not make anything up.
                Only use the context you are provided. 
                Also, don't let it look obvious that you are a bot.
                
                context: {context} 
                Question: {input}
                """)

    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', prompt_template),
            ('human', "{input}")
        ]
    )
    
    document = pdf_loader(context)
    retriever = get_retriever(document)
    
    question_answer_chain = create_stuff_documents_chain(gemini_llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({'input': user_prompt})
    
    return response