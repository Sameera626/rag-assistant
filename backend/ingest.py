import os
from backend.utils import load_documents_from_dir, split_documents, get_embeddings
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

DATA_DIR = './data'
EMBED_MODEL = os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_INDEX = os.getenv('PINECONE_INDEX', 'langchain-demo')  # Set your Pinecone index name

def main():
    docs = load_documents_from_dir(DATA_DIR)
    print(f"Loaded {len(docs)} raw documents")
    if not docs:
        print("No documents found. Exiting.")
        return
    chunks = split_documents(docs)
    print(f"split into {len(chunks)} chunks")

    emb = get_embeddings(model_name=EMBED_MODEL)
    # Get embeddings for each chunk
    texts = [chunk.page_content for chunk in chunks]
    # print(texts)
    metadatas = []
    for chunk in chunks:
        meta = dict(chunk.metadata) if chunk.metadata else {}
        print(meta)
        if 'text' not in meta:
            meta['text'] = chunk.page_content
            print(meta)
        metadatas.append(meta)
    vectors = emb.embed_documents(texts)


    # Initialize Pinecone client
    pc = Pinecone(api_key=PINECONE_API_KEY)
    # Check if index exists, create if not
    if PINECONE_INDEX not in pc.list_indexes().names():
        pc.create_index(
            name=PINECONE_INDEX,
            dimension=len(vectors[0]),
            metric='cosine', 
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    index = pc.Index(PINECONE_INDEX)

    # Prepare and upsert vectors
    pinecone_vectors = []
    for i, (vec, meta) in enumerate(zip(vectors, metadatas)):
        pinecone_vectors.append((str(i), vec, meta))
    index.upsert(vectors=pinecone_vectors)
    print(f'{len(pinecone_vectors)} vectors upserted to Pinecone index "{PINECONE_INDEX}"')

if __name__ == '__main__':
    main()