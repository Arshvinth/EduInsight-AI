# 🚀 EduInsight-AI

An AI-powered backend system for student performance analysis, RAG-based responses, and ML-driven predictions using FastAPI, PostgreSQL (pgvector), and Google Gemini.

---

## 📁 Project Structure

```
.
├── backend/
├── ml/
├── docker-compose.yml
└── README.md
```

---

## 🚫 .gitignore

```
node_modules/
dist/
__pycache__/
*.pyc
*.env*
venv/
*.DS_Store
Thumbs.db
ml/models/*.pkl
ml/data/raw/
ml/data/processed/
```

---

## ⚙️ Backend Setup

### 1. Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

### 2. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-multipart pandas scikit-learn joblib numpy sentence-transformers google-generativeai tika pgvector
```

---

## 🐳 Docker Setup (Database Layer)

| Service               | Purpose     | Port |
| --------------------- | ----------- | ---- |
| PostgreSQL + pgvector | AI database | 5432 |
| pgAdmin 4             | DB UI tool  | 5050 |

---

### Start Services

```bash
docker compose up -d
```

### Stop Services (keep data)

```bash
docker compose stop
```

### Restart Services

```bash
docker compose start
```

### Shutdown Containers

```bash
docker compose down
```

### Shutdown + Delete Data

```bash
docker compose down -v
```

---

## 🚀 Run FastAPI Backend

From the `backend/` folder:

```bash
uvicorn app.main:app --reload
```

---

## 🧠 Features

* 📊 Student performance prediction (ML model)
* 🤖 RAG-based AI response system
* 🧬 Vector database support (pgvector)
* ⚡ FastAPI high-performance backend
* 🐳 Dockerized database layer

---

## 🛡️ Notes

* Keep `.env` file **never committed**
* Rotate API keys if previously exposed
* Ensure Docker is running before backend startup

---
