import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.chat_models import ChatOpenAI
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from pinecone import Pinecone
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_classic.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
EMBED_MODEL = os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small')
LLM_MODEL = os.getenv('LLM_MODEL', 'gpt-4o-mini')

# Pinecone config from environment
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX = os.getenv('PINECONE_INDEX')

emb = OpenAIEmbeddings(model=EMBED_MODEL, api_key=OPENAI_API_KEY)

# Initialize Pinecone client and index
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

# Setup LangChain Pinecone vectorstore
vectordb = LangchainPinecone(
    index,
    emb,
    'text'  
)
retriever = vectordb.as_retriever(search_kwargs={"k": 4})
llm = ChatOpenAI(model=LLM_MODEL, temperature=0, api_key=OPENAI_API_KEY)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key='answer')

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    verbose=True
)

class Query(BaseModel):
    question: str
   

@app.post('/query')
async def query(q: Query):
    result = qa_chain({"question": q.question})
    return {'answer': result['answer']}
