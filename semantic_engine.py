from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def rank_relevance(query, text_blocks):

    texts = [
        item["text"]
        for item in text_blocks
    ]

    query_embedding = model.encode([query])

    text_embeddings = model.encode(texts)

    similarities = cosine_similarity(
        query_embedding,
        text_embeddings
    )[0]

    ranked = []

    for item, score in zip(text_blocks, similarities):

        ranked.append({
            "text": item["text"],
            "coords": item["coords"],
            "confidence": item["confidence"],
            "relevance": float(score)
        })

    ranked.sort(
        key=lambda x: x["relevance"],
        reverse=True
    )

    return ranked
