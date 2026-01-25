# DEV_GUIDE.md — HomeFlix Phase-0 Quickstart

# Developer Quickstart — Phase-0

## 1️⃣ Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd homeflix
```

---

## 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Linux/macOS
# .\venv\Scripts\activate     # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 3️⃣ Frontend Setup

```bash
cd ../frontend
npm install
npm start
```

- React dev server runs at `http://localhost:3000`

---

## 4️⃣ Run Backend

```bash
cd backend
python run.py
```

- FastAPI runs at `http://127.0.0.1:8000`  
- API docs: `http://127.0.0.1:8000/docs`

---

## 5️⃣ Available Endpoints (Phase-0)

- `/auth/ping` → test auth router  
- `/profiles/` → list profiles  
- `/media/` → list media  

Tables auto-created on first run.

---

## 6️⃣ GitHub Workflow

```bash
git add .
git commit -m "Phase-0 backend skeleton with run.py, models, routers, and React frontend template"
git push
```

---

## 7️⃣ Notes / Tips

- Backend uses **FastAPI + SQLAlchemy + SQLite**  
- Frontend is a **React template** ready to connect  
- `run.py` replaces manual `uvicorn` command  
- Phase-0 is **skeleton only**, no media ingestion or device auth yet

---

## 8️⃣ Next Steps

1. Add **seed profiles & media items**  
2. Implement **device auth / JWT**  
3. Connect React frontend to API  
4. Plan for **Docker + Postgres migration** in Phase-1
