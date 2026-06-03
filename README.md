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
cd backend
```
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
cd ..
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


---
Postman

http://localhost:8000/

POST /auth/register
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "123456",
  "role": "student"
}

POST /auth/login
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "123456",
  "role": "student"
}
{
  "username": "admin1",
  "email": "admin1@example.com",
  "password": "123456",
  "role": "admin"
}
{
  "username": "faculty1",
  "email": "faculty1@example.com",
  "password": "123456",
  "role": "faculty"
}

It will return:
{
  "access_token": "your.jwt.token",
  "token_type": "bearer"
}

Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json

POST /modules/
{
  "module_code": "CS101",
  "module_name": "Introduction to Programming",
  "credits": 3,
  "department": "Computer Science",
  "semester": 1
}

PUT /modules/1
{
  "module_code": "CS101",
  "module_name": "Intro to Programming",
  "credits": 4,
  "department": "Computer Science",
  "semester": 1
}


POST /enrollments/
{
  "module_id": 1,
  "status": "enrolled"
}

Authorization: Bearer YOUR_STUDENT_TOKEN

GET /enrollments/me

Authorization: Bearer YOUR_ADMIN_OR_FACULTY_TOKEN
Content-Type: application/json

admin/faculty token and call:
PUT /students/{Student_ID}

{
  "full_name": "Updated Student Name",
  "department": "Computer Science",
  "registered_degree": "BSc Computer Science",
  "specialization": "AI",
  "semester": 3,
  "year": 2,
  "cgpa": 3.5
}

Authorization: Bearer YOUR_ADMIN_OR_FACULTY_TOKEN
Content-Type: application/json

POST /attendance/
{
  "student_id": 1,
  "module_id": 1,
  "status": "present",
  "attendance_date": "2026-06-02"
}

Authorization: Bearer YOUR_STUDENT_TOKEN

View own attendance
GET /attendance/me

Bearer YOUR_FACULTY_OR_ADMIN_TOKEN

POST /results/
{
  "student_id": 1,
  "module_id": 1,
  "marks": 78.5,
  "grade": "A",
  "semester": 2,
  "year": 1
}

GET /results/me

Authorization: Bearer YOUR_TOKEN
Content-Type: application/json

POST /ai/upload-document
Body
Select:

Body
form-data
Add fields:

Key	Type	Value
file	File	choose a PDF or DOCX
title	Text	optional title

response:
{
  "id": 1,
  "filename": "my_notes.pdf",
  "file_path": "backend/uploads/my_notes.pdf",
  "title": "Attendance Policy",
  "created_at": "2026-06-02T10:00:00"
}


POST /ai/chat
{
  "query": "What is the attendance policy?"
}

output:
{
  "query": "What is the attendance policy?",
  "answer": "Based on the available documents...",
  "context_used": true,
  "matched_chunks": [
    "..."
  ]
}

POST /ml/predict-risk
{
  "attendance": 61,
  "cgpa": 5.8,
  "failed_modules": 1,
  "recent_marks": 54
}

response:
{
  "prediction": "at_risk",
  "risk_score": 0.87
}

Model training
pip install pandas scikit-learn joblib numpy 
python app/ml/train_risk_model.py

























