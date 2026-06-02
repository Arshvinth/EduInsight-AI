from sqlalchemy.orm import Session
from app.crud.document import get_all_documents


# Very simple retrieval function for now
# In the future, replace this with embeddings + vector search
def retrieve_relevant_context(db: Session, query: str) -> str:
    documents = get_all_documents(db)

    # Naive keyword-based matching for initial RAG setup
    matched_chunks = []

    for doc in documents:
        content_lower = doc.content.lower()
        query_lower = query.lower()

        # If query terms appear in document content, include it
        if any(word in content_lower for word in query_lower.split()):
            snippet = doc.content[:1000]  # limit size
            matched_chunks.append(f"Document: {doc.filename}\n{snippet}")

    if not matched_chunks:
        return ""

    return "\n\n".join(matched_chunks)


# Placeholder response generator
# Later this can call OpenAI, local LLM, or another model
def generate_answer(query: str, context: str) -> str:
    if not context:
        return "I could not find relevant information in the uploaded documents."

    return (
        "Based on the available documents, here is the most relevant context:\n\n"
        f"{context[:2000]}\n\n"
        f"Question: {query}"
    )