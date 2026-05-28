import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()

collection = client.create_collection(
    name="cortex_memory"
)

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def store_paragraphs(paragraphs):

    for i, para in enumerate(paragraphs):

        embedding = model.encode(
            para["text"]
        ).tolist()

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[para["text"]]
        )

def query_memory(query, top_k=5):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results
