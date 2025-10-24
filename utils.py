from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def load_documents_from_dir(path: str):
    docs = []
    for fn in os.listdir(path):
        full = os.path.join(path, fn)
        if fn.lower().endswith('.pdf'):
            loader = PyPDFLoader(full)
            print(loader.load())
            docs.extend(loader.load())
        elif fn.lower().endswith('.txt'):
            loader = TextLoader(full)
            docs.extend(loader.load())
    return docs

def split_documents(docs, chunk_size=800, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

def get_embeddings(model_name: str = None):
    return OpenAIEmbeddings(model=model_name, api_key=OPENAI_API_KEY)