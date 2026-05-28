from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def discover_topics(paragraphs, n_clusters=3):

    texts = [
        para["text"]
        for para in paragraphs
    ]

    embeddings = model.encode(texts)

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42
    )

    labels = kmeans.fit_predict(
        embeddings
    )

    clustered = {}

    for label, text in zip(labels, texts):

        if label not in clustered:

            clustered[label] = []

        clustered[label].append(text)

    return clustered
