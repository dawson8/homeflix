# HomeFlix — Developer Quickstart (Phase-0)

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
uvicorn app.main:app --reload
```

- FastAPI runs at `http://127.0.0.1:8000`  
- API docs: `http://127.0.0.1:8000/docs`

---

## 5️⃣ GitHub Workflow

```bash
git add .
git commit -m "Phase-0 initial setup: backend + frontend"
git push -u origin main
```

---

## ✅ Notes / Tips

- Backend uses **FastAPI + SQLAlchemy + JWT + SQLite**  
- Frontend is a **React template** ready for viewer/admin UI  
- Virtual environment **isolates dependencies**  
- Phase-0 is **skeleton only**, no media ingestion or profiles yet  
- Keep `.gitignore` updated to avoid committing `venv` or `node_modules`  

---

## 6️⃣ Next Steps

1. Build **backend skeleton** (`main.py`, `db.py`, `models.py`, routers)  
2. Add **profiles + media seed data**  
3. Implement **device auth + JWT**  
4. Connect React frontend to API  
5. Start **viewer vs admin capability enforcement**
