from langchain_chroma import Chroma  # a vector db to store embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # to create embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_document(document, chunk_size):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size)
    chunks = splitter.split_documents(document)
    return chunks

def get_vectorstore(document, chunk_size, model):
    chunks = split_document(document, chunk_size)
    # apply the embeddings to entire document chucks then store in a vectorStore using chroma
    vectorstore = Chroma.from_documents(documents=chunks, embedding=GoogleGenerativeAIEmbeddings(model=model))
    return vectorstore

def get_retriever(document, k=10, chunk_size=200, model: str='models/embedding-001'):
    # if not vectorstore initialize one and save it
    vectorstore = get_vectorstore(document, chunk_size=chunk_size, model=model)
    # search similar docs
    retriever = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k': k})
    return retriever
