# Chunking Strategies Analyser

A web application to visualize and compare different text chunking strategies used in NLP and RAG (Retrieval-Augmented Generation).

## Features

- Upload PDF, DOCX, TXT, CSV, XLSX files
- Extract text from uploaded documents
- Compare multiple chunking strategies:
  - Fixed Size Chunking
  - Fixed Size + Overlap
  - Sentence-Based Chunking
  - Recursive Chunking
  - Semantic Chunking
- FastAPI backend
- Streamlit frontend

---

## Project Structure

```
Chunking_stratagies_analyser/
│
├── backend_analyser/
│   ├── api.py
│   ├── chunking.py
│   ├── file_reader.py
│   
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# Prerequisites

Install:

- Python 3.10 or above
- Git

---

# Clone the Repository

```bash
git clone https://github.com/Saimohan80747/Chuncking_stratagies_analyser.git
```

```bash
cd Chuncking_stratagies_analyser
```

---

# Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Command Prompt

```cmd
.venv\Scripts\activate
```

---

# Install Dependencies
/backend_analyser
```bash
pip install -r requirements.txt
```
/frontend_analyser
```bash
pip install -r requirements.txt
```
---



---



# Run Backend (FastAPI)

Open a terminal.

Activate the virtual environment.

Run:

```bash
cd backend_analyser
```

```bash
uvicorn api:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# Run Frontend (Streamlit)

Open another terminal.

Activate the same virtual environment.

Run:

```bash
streamlit run frontend/app.py
```

The application opens automatically in your browser.

Default URL:

```
http://localhost:8501
```

---

# Supported File Types

- PDF
- DOCX
- TXT
- CSV
- XLSX
- XLS

---

# Chunking Strategies

## Fixed Size

Splits text into equal-sized chunks.

---

## Fixed Size + Overlap

Creates overlapping chunks to preserve context.

---

## Sentence-Based

Groups complete sentences together.

---

## Recursive

Recursively splits large paragraphs into smaller chunks.

---

## Semantic

Uses sentence embeddings and cosine similarity to group semantically similar sentences.

---

# Technologies Used

- Python
- FastAPI
- Streamlit
- Sentence Transformers
- spaCy
- scikit-learn
- NumPy
- pandas
- PyPDF
- python-docx

---

# Install New Dependencies

After activating the virtual environment:

```bash
pip install package_name
```

Update requirements:

```bash
pip freeze > requirements.txt
```

---

# Stop the Servers

Press:

```
Ctrl + C
```

in both backend and frontend terminals.

---

# Author

**Saimohan**

GitHub:

https://github.com/Saimohan80747
