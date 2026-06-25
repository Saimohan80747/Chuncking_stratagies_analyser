from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
import re
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
openai_api_key = os.getenv("OPENAI_API_KEY")

def fixed_chunks(text, chunk_size):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks

def overlap_chunks(text, chunk_size, overlap_size):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        start += chunk_size - overlap_size-1

    return chunks

def sentence_chunks(text, sentences_per_chunk=1):
    
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    chunks = []

    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = " ".join(sentences[i:i + sentences_per_chunk])
        chunks.append(chunk)

    return chunks

def recursive_chunks(text, chunk_size=5):
    chunks = []

    paragraphs = text.split("\n\n")

    for para in paragraphs:

        if len(para) <= chunk_size:
            chunks.append(para)
            continue
        else:
            chunks+=sentence_chunks(para);

    return chunks

def semantic_chunks(text):
    if not text or not text.strip():
        return []

    try:
        embeddings = OpenAIEmbeddings(api_key=openai_api_key)
        splitter = SemanticChunker(embeddings,breakpoint_threshold_type="percentile")
        docs = splitter.create_documents([text])
        return [doc.page_content for doc in docs]
    except Exception as exc:
        print(f"Semantic chunking unavailable, using sentence split instead: {exc}")
        return sentence_chunks(text)