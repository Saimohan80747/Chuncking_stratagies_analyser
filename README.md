# Chunking Strategies Analyser

A Python project to analyze and compare different **text chunking strategies** for NLP/LLM workflows.

## 📌 Overview

When working with large documents, the way you split text into chunks can significantly affect downstream tasks like:

- Retrieval-Augmented Generation (RAG)
- Semantic search
- Embedding quality
- Context efficiency for LLMs

This project helps evaluate and analyze various chunking methods so you can choose the best strategy for your use case.

## ✨ Features

- Compare multiple chunking strategies
- Analyze chunk size, overlap, and coverage
- Evaluate chunk distribution and consistency
- Simple Python-based workflow
- Easy to extend with custom chunkers

## 🛠️ Tech Stack

- **Language:** Python

## 📁 Project Structure

```text
Chuncking_stratagies_analyser/
├── README.md
├── (your source files)
└── (optional notebooks / data / outputs)
```

## 🚀 Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/Saimohan80747/Chuncking_stratagies_analyser.git
cd Chuncking_stratagies_analyser
```

### 2) Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies

If you have a requirements file:

```bash
pip install -r requirements.txt
```

If not, install your current dependencies manually.

### 4) Run the project

```bash
python main.py
```

> Update the command above based on your actual entry-point file.

## 🧪 Example Use Cases

- Testing fixed-size vs semantic chunking
- Measuring overlap impact on retrieval
- Finding optimal chunk size for a specific model
- Preprocessing long PDFs/articles before embedding

## 🔧 Configuration Ideas

You can tune parameters such as:

- `chunk_size`
- `chunk_overlap`
- separator rules
- sentence/paragraph boundaries
- token-based vs character-based splitting

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## 📄 License

Add your preferred license here (e.g., MIT).

## 👤 Author

**Saimohan80747**  
GitHub: https://github.com/Saimohan80747
