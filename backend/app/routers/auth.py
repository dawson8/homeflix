# ===============================
# backend/app/routers/auth.py
# ===============================

from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "Auth router is alive!"}
