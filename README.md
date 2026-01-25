# README.md — HomeFlix (Phase-0)

# HomeFlix — Family-Focused Media Server

HomeFlix is a **self-hosted, family-friendly media platform** inspired by modern streaming services.  

**Phase-0** includes a **backend skeleton** (FastAPI + SQLite), a **React frontend template**, and GitHub repo setup. This version is primarily for **development and testing**.

---

## Project Structure

```text
homeflix/
├─ backend/               # Python backend (FastAPI)
│  ├─ app/
│  ├─ run.py              # Script to start backend
│  ├─ requirements.txt
│  └─ venv/
├─ frontend/              # React frontend template
├─ .gitignore
├─ README.md
└─ DEV_GUIDE.md           # Developer quickstart
```

---

## Phase-0 Highlights

- **Backend skeleton** with FastAPI routers:
  - `/auth` → placeholder for device authentication
  - `/profiles` → list/select profiles
  - `/media` → list media
- **Database**: SQLite (`homeflix.db`), tables auto-created on startup
- **Frontend**: React template ready for viewer/admin UI
- **Run backend**: `python backend/run.py`
- **Run frontend**: `npm start` in `frontend/`

---

## Next Steps

- Seed initial **profiles** and **media items**  
- Implement **device authentication (JWT)**  
- Connect frontend to backend API  
- Prepare for **Phase-1 Docker/Postgres deployment**
