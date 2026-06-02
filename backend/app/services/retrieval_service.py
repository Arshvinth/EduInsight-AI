from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models.document import DocumentChunk
from app.services.embedding_service import create_embedding


# Retrieve top-k most relevant chunks for a query
def retrieve_top_k_chunks(db: Session, query: str, k: int = 5):
    query_embedding = create_embedding(query)

    # Order by vector similarity using pgvector
    # Smaller distance means more similar
    results = (
        db.query(DocumentChunk)
        .order_by(DocumentChunk.embedding.cosine_distance(query_embedding))
        .limit(k)
        .all()
    )

    return results