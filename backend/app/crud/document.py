from sqlalchemy.orm import Session
from app.models.document import Document, DocumentChunk


# Create a document record
def create_document(db: Session, filename: str, file_path: str, title: str | None = None):
    document = Document(
        filename=filename,
        file_path=file_path,
        title=title
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


# Create many chunks for a document
def create_document_chunks(db: Session, document_id: int, chunks_with_embeddings: list[tuple[str, list[float]]]):
    created_chunks = []

    for idx, (chunk_text, embedding) in enumerate(chunks_with_embeddings):
        chunk = DocumentChunk(
            document_id=document_id,
            chunk_index=idx,
            chunk_text=chunk_text,
            embedding=embedding
        )
        db.add(chunk)
        created_chunks.append(chunk)

    db.commit()

    for chunk in created_chunks:
        db.refresh(chunk)

    return created_chunks


# Get all chunks for retrieval
def get_all_chunks(db: Session):
    return db.query(DocumentChunk).all()