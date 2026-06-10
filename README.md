# WineGPT 🍷

A simple AI-powered wine recommendation assistant built with FastAPI, ChromaDB, embeddings, and an LLM.

## Features

- Wine recommendations
- Food pairing suggestions
- Wine comparisons
- Semantic search with vector embeddings
- Retrieval-Augmented Generation (RAG)

## Tech Stack

- Python
- FastAPI
- ChromaDB
- LangChain
- Sentence Transformers
- OpenAI API

## Setup

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Build the vector database:

```bash
python rag/vectorstore.py
```

Run the API:

```bash
uvicorn app:app --reload
```

Visit:

```text
http://127.0.0.1:8000/docs
```

## Example Endpoints

```http
GET /recommend?query=wine+for+steak

GET /pairing?food=lobster

GET /compare?wine_a=Pinot+Noir&wine_b=Cabernet+Sauvignon
```

## Disclaimer

This is a demonstration project created for portfolio and social media purposes only. It is not a real production application and does not represent any proprietary, client, employer, or business-critical systems. The implementation is intentionally simplified to showcase AI engineering concepts.