# 📄 Chunking Strategies Analyzer

A full-stack application for analyzing and visualizing different text chunking strategies. Compare how various chunking methods segment your documents.

## 📋 Features

- **Multiple Chunking Strategies:**
  - Fixed Size — chunk by character count
  - Fixed Size + Overlap — fixed chunks with overlapping content
  - Sentence Based — split by sentences
  - Recursive — split by paragraphs, then sentences
  - Semantic — AI-powered topic-based chunking (OpenAI embeddings)

- **File Upload Support:**
  - PDF, CSV, Excel (XLSX, XLS), DOCX, TXT
  - Direct text input

- **Interactive UI:**
  - Streamlit frontend
  - Real-time chunking preview
  - Side-by-side comparison

- **REST API Backend:**
  - FastAPI with async support
  - Scalable chunking endpoints

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key (for semantic chunking)

### Installation

1. **Clone/navigate to the project:**
   ```powershell
   cd c:\Users\saimohane\saimohan\chunking_stratagies_analyser
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r venv/requirement.txt
   ```

3. **Set OpenAI API key:**
   ```powershell
   $env:OPENAI_API_KEY="your_api_key_here"
   ```

### Running the Application

**Run from the project root** (`chunking_stratagies_analyser/` folder):

1. **Start the backend (FastAPI):**
   ```powershell
   uvicorn backend_analyser.api:app --reload --port 8000
   ```
   - API will be available at `http://127.0.0.1:8000`
   - Docs at `http://127.0.0.1:8000/docs`

2. **In a new terminal, start the frontend (Streamlit):**
   ```powershell
   streamlit run frontend_analyser/app.py
   ```
   - UI will open at `http://localhost:8501`

---

## 📁 Project Structure

```
chunking_stratagies_analyser/
├── backend_analyser/
│   ├── api.py                 # FastAPI endpoints
│   ├── chunking.py            # Chunking algorithms
│   └── file_reader.py         # File extraction
│
├── frontend_analyser/
│   └── app.py                 # Streamlit UI
│
├── venv/
│   └── requirement.txt        # Dependencies
│
├── nlp/
│   └── basics.ipynb          # Reference notebook
│
└── README.md                 # This file
```

---

## 🔧 API Endpoints

### POST `/chunk`

Chunk text using a specified strategy.

**Request:**
```json
{
  "text": "Your text here...",
  "strategy": "Semantic",
  "chunk_size": 100,
  "overlap_size": 20
}
```

**Response:**
```json
{
  "strategy": "Semantic",
  "total_chunks": 3,
  "chunks": ["chunk1", "chunk2", "chunk3"]
}
```

### POST `/file`

Extract text from an uploaded file.

**Request:** (multipart form-data)
```
file: <binary file>
```

**Response:**
```json
{
  "text": "extracted text..."
}
```

---

## 📊 Chunking Strategies Explained

### Fixed Size
Splits text into chunks of exact character length.
- **Use case:** uniform-sized data streams
- **Parameter:** `chunk_size` (characters)

### Fixed Size + Overlap
Fixed chunks with overlapping boundaries to preserve context.
- **Use case:** sliding-window analysis
- **Parameters:** `chunk_size`, `overlap_size`

### Sentence Based
Splits by sentence boundaries; groups multiple sentences per chunk.
- **Use case:** natural language processing
- **Parameter:** `sentences_per_chunk`

### Recursive
First splits by paragraphs, then applies sentence-based chunking within each.
- **Use case:** structured documents (essays, articles)

### Semantic
AI-powered topic-aware chunking using OpenAI embeddings.
- **Use case:** keeping related content together
- **Algorithm:** centroid-based topic boundary detection
- **Requires:** OpenAI API key

---

## 🛠️ Configuration

### Environment Variables

```powershell
# OpenAI API Key (required for semantic chunking)
$env:OPENAI_API_KEY="sk-..."

# Optional: Change API port
$env:API_PORT="8000"

# Optional: Change Streamlit port
$env:STREAMLIT_SERVER_PORT="8501"
```

### Dependencies (venv/requirement.txt)

```
streamlit>=1.28.0
fastapi>=0.104.0
uvicorn>=0.24.0
pandas>=2.0.0
pypdf>=3.17.0
python-docx>=0.8.11
langchain-experimental>=0.0.50
langchain-openai>=0.0.5
sentence-transformers>=2.2.0
```

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'backend_analyser'`

**Solution:** Run Streamlit and FastAPI from the project root:
```powershell
cd chunking_stratagies_analyser
streamlit run frontend_analyser/app.py
```

### `Error extracting text: not enough values to unpack`

**Solution:** Ensure the backend is running:
```powershell
uvicorn backend_analyser.api:app --reload --port 8000
```

### `Semantic chunking unavailable, using sentence split instead`

**Possible causes:**
- OpenAI API key not set: `$env:OPENAI_API_KEY="your_key"`
- API quota exceeded or invalid key
- Network connectivity issue

### `Cannot connect to backend`

**Solution:** Ensure the FastAPI server is running on port 8000:
```powershell
uvicorn backend_analyser.api:app --reload --port 8000
```

---

## 📝 Example Usage

### Command Line (API)
```bash
curl -X POST http://127.0.0.1:8000/chunk \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Python is great. Cricket is fun. Machine learning is complex.",
    "strategy": "Semantic",
    "chunk_size": 100
  }'
```

### Using the UI
1. Open `http://localhost:8501`
2. Upload a file or paste text
3. Select a chunking strategy
4. Adjust parameters if needed
5. Click "Generate [Strategy] Chunks"
6. View results in expandable chunks

---

## 🤝 Contributing

To extend with new chunking strategies:

1. Add the function to `backend_analyser/chunking.py`
2. Add a case in `backend_analyser/api.py` `/chunk` endpoint
3. Add UI controls in `frontend_analyser/app.py`
4. Test the endpoint with curl or the UI

---

## 📄 License

MIT

---

## ❓ Questions?

- Check API docs: `http://127.0.0.1:8000/docs`
- View chunking algorithms: `backend_analyser/chunking.py`
- Check file extraction: `backend_analyser/file_reader.py`

