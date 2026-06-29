from pydantic import BaseModel
from fastapi import FastAPI,UploadFile, File

from chunking import (
    fixed_chunks,
    overlap_chunks,
    sentence_chunks,
    recursive_chunks,
    semantic_chunks
)
from file_reader import extract_text
from classes import ChunkRequest,TokenRequest,PipeLine

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

class TokenRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Chunking API is running successfully"
    }

@app.post("/file")
async def upload_file(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}")
    print(f"File content type: {file.content_type}")
    extracted_text = extract_text(file)
    return {"text": extracted_text}

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

@app.post("/pipeline"):
def pipeline(file:UploadFile=File(...):
   pipeline=PipeLine([upload_file,chunk_text])
   result=pipeline.run(file)
   return result
    
# @app.post("/tokenize")
# def tokenize_text(data: TokenRequest):
#     doc = tokenise_text(data.text)
#     return {"tokens": [token.text for token in doc]}

# @app.post("/embeddings")
# def get_embeddings(data: TokenRequest):
#     try:
#         embeddings = OpenAIEmbeddings(api_key=openai_api_key)
#         vector = embeddings.embed_query(data.text)
#         return {"embedding": vector}
#     except Exception as exc:
#         return {"error": f"Failed to get embeddings: {exc}"}
