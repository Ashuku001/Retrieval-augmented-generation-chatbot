from langchain_community.document_loaders import PyPDFLoader

def get_document(path):
    loader = PyPDFLoader(path)
    document = loader.load()  # load the entire pdf
    return document