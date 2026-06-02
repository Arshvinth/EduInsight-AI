from sentence_transformers import SentenceTransformer


# Load a local embedding model once
# This model produces 384-dimensional vectors
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Convert text into a vector embedding
def create_embedding(text: str) -> list[float]:
    # Convert text to embedding vector
    vector = embedding_model.encode(text, normalize_embeddings=True)

    # Convert numpy array to plain Python list
    return vector.tolist()