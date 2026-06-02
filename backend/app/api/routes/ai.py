from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Body
from sqlalchemy.orm import Session
import os
import shutil
from pathlib import Path

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.document import ChatResponse, DocumentRead, ChatRequest
from app.services.extraction_service import extract_text_from_file, get_file_extension
from app.services.chunking_service import chunk_text
from app.services.embedding_service import create_embedding
from app.services.retrieval_service import retrieve_top_k_chunks
from app.services.gemini_service import generate_answer_with_gemini
from app.crud.document import create_document, create_document_chunks
from app.models.document import Document


# Router for AI/RAG endpoints
router = APIRouter(prefix="/ai", tags=["AI"])

# Folder where uploaded files are stored
UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# Upload a PDF or DOCX document for RAG
@router.post("/upload-document", response_model=DocumentRead)
def upload_document(
    file: UploadFile = File(...),
    title: str | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Validate file type
    ext = get_file_extension(file.filename)
    if ext not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are allowed")

    # Save uploaded file to disk
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from file
    extracted_text = extract_text_from_file(str(file_path))
    if not extracted_text:
        raise HTTPException(status_code=400, detail="Could not extract text from the file")

    # Create document record
    document = create_document(db, file.filename, str(file_path), title)

    # Chunk extracted text
    chunks = chunk_text(extracted_text)

    # Create embeddings for each chunk
    chunks_with_embeddings = []
    for chunk in chunks:
        embedding = create_embedding(chunk)
        chunks_with_embeddings.append((chunk, embedding))

    # Store chunks in database
    create_document_chunks(db, document.id, chunks_with_embeddings)

    return document


# Chat endpoint that uses retrieved chunks + Gemini
@router.post("/chat", response_model=ChatResponse)
def chat_with_ai(
    payload: ChatRequest = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        # Retrieve top relevant chunks
        query = payload.query
        matched_chunks = retrieve_top_k_chunks(db, query, k=5)

        # Build context from retrieved chunks
        context = "\n\n".join([f"[Doc {c.document_id} - Chunk {c.chunk_index}]\n{c.chunk_text}" for c in matched_chunks])

        # Generate answer
        answer = generate_answer_with_gemini(query, context)

        return {
            "query": query,
            "answer": answer,
            "context_used": bool(context),
            "matched_chunks": [c.chunk_text for c in matched_chunks]
        }
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        print(tb)
        raise HTTPException(status_code=500, detail=str(e))


# What this does

# uploads docs
# validates PDF/DOCX
# stores file on disk
# extracts text
# chunks text
# embeds chunks
# stores everything
# answers chat queries with retrieved context

# Upload side
# User uploads PDF/DOCX
# File is saved to disk
# Apache Tika extracts text
# Text is chunked
# Each chunk is embedded
# Chunks are stored in pgvector

# Query side
# User asks a question
# Question is embedded
# Vector search fetches top-k chunks
# Gemini gets the retrieved context
# Final answer is returned