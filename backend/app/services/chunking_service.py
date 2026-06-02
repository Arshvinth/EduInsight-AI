

# Split text into overlapping chunks for retrieval
def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    chunks = []

    if not text:
        return chunks

    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # Move forward with overlap
        start += chunk_size - overlap

    return chunks