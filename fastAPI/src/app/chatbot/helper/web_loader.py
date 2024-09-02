from langchain_community.document_loaders import UnstructuredURLLoader

async def get_document(urls: list[str])
    loader = UnstructuredURLLoader(urls=urls)
    document = loader.load()
    return document