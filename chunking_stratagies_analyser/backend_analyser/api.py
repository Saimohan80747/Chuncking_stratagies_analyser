from fastapi import FastAPI
from pydantic import BaseModel

from chunking import (
    fixed_chunks,
    overlap_chunks,
    sentence_chunks,
    recursive_chunks,
    semantic_chunks
)

app = FastAPI(
    title="Chunking API",
    description="API for different text chunking strategies",
    version="1.0.0"
)


class ChunkRequest(BaseModel):
    text: str
    strategy: str
    chunk_size: int = 100
    overlap_size: int = 20


@app.get("/")
def home():
    return {
        "message": "Chunking API is running"
    }


@app.post("/chunk")
def chunk_text(data: ChunkRequest):

    text = data.text.strip()

    if not text:
        return {
            "error": "Text cannot be empty"
        }

    if data.strategy == "Fixed Size":

        chunks = fixed_chunks(
            text,
            data.chunk_size
        )

    elif data.strategy == "Fixed Size + Overlap":

        chunks = overlap_chunks(
            text,
            data.chunk_size,
            data.overlap_size
        )

    elif data.strategy == "Sentence Based":

        chunks = sentence_chunks(
            text,
            data.chunk_size
        )

    elif data.strategy == "Recursive":

        chunks = recursive_chunks(text)

    elif data.strategy == "Semantic":

        chunks = semantic_chunks(text)

    else:

        return {
            "error": f"Unknown strategy: {data.strategy}"
        }

    return {
        "strategy": data.strategy,
        "total_chunks": len(chunks),
        "chunks": chunks
    }