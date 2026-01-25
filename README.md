# HomeFlix — Phase-0 Developer Guide

## Overview

HomeFlix is a **family-focused, self-hosted media server**.  
Phase-0 is a minimal working setup with:

- Backend (Python + FastAPI)  
- Frontend (React template)  
- Device and profile support  
- Basic media endpoint  
- GitHub version control

This guide explains how we **got here** and how to run the project.

---

## Folder Structure

```text
homeflix/
├─ backend/               # Python backend
│  ├─ app/
│  ├─ requirements.txt
│  └─ venv/               # Virtual environment
├─ frontend/              # React frontend template
│  ├─ src/
│  ├─ package.json
│  └─ node_modules/
├─ .gitignore
└─ README.md
```

---

## Setup Steps (Phase-0)

### 1. Clone Repo

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd homeflix
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Linux/macOS
# .\venv\Scripts\activate     # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
```

---

## Run Project (Phase-0)

### Backend

```bash
cd backend
uvicorn app.main:app --reload
```

- FastAPI server runs at `http://127.0.0.1:8000`  
- Open `http://127.0.0.1:8000/docs` for API docs (Swagger)

### Frontend

```bash
cd frontend
npm start
```

- React dev server runs at `http://localhost:3000`

---

## GitHub Integration

1. Add `.gitignore` before committing.
2. Stage & commit everything:

```bash
git add .
git commit -m "Phase-0 initial setup: backend + frontend skeleton"
git push -u origin main
```

---

## Notes / Lessons Learned

- **Dependency conflicts:** FastAPI requires `python-multipart>=0.0.7`. Always check package requirements.  
- **Virtual environment:** Keeps Python dependencies isolated.  
- **Frontend template:** React is ready for building the viewer/admin UI.  
- **Phase-0:** Only skeleton code, no media ingestion, authentication, or profiles yet.  

---

## Next Steps

1. Create **FastAPI backend skeleton** with `main.py`, `db.py`, `models.py`, and basic routers.  
2. Seed **profiles** (adult + kids) and a few **media items**.  
3. Implement **device authentication** (JWT + pairing).  
4. Connect React frontend to the API.  
5. Start building **viewer vs admin capability enforcement**.

