import re
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_chunks(text):
    sentences= sentence_chunks(text)

    model = SentenceTransformer("all-MiniLM-L6-v2")


    vis = [False] * len(sentences)
    embeddings = model.encode(sentences)

    chunks = []

    threshold = 0.25

    for i in range(0, len(sentences)):
        if vis[i]:
            continue
        chunks.append([i])
        for j in range(i+1, len(sentences)):
            if vis[j]:
                continue
            current_chunk_vectors = embeddings[chunks[-1]]
            centroid = np.mean(current_chunk_vectors, axis=0)
            sim = cosine_similarity(
                [embeddings[j]],
                [centroid]
            )[0][0]
            if sim >= threshold:
                chunks[-1].append(j)
                vis[j] = True
                



    for idx, chunk in enumerate(chunks):
        print(f"\nChunk {idx+1}")
        print("-"*20)
        for s in chunk:
            print(sentences[s])

    return [" ".join([sentences[s] for s in chunk]) for chunk in chunks]


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

