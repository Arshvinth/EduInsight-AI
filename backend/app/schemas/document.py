from pydantic import BaseModel
from datetime import datetime
from typing import List


# Used when returning a document
class DocumentRead(BaseModel):
    id: int
    filename: str
    file_path: str
    title: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


# Used when returning a chunk
class DocumentChunkRead(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    chunk_text: str
    created_at: datetime

    class Config:
        from_attributes = True


# Response for AI answers
class ChatResponse(BaseModel):
    query: str
    answer: str
    context_used: bool
    matched_chunks: List[str]


# Request model for chat endpoint
class ChatRequest(BaseModel):
    query: str

    class Config:
        schema_extra = {"example": {"query": "What is polymorphism?"}}