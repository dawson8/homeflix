# ===============================
# backend/app/routers/profiles.py
# ===============================

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, db

router = APIRouter()

# Dependency
def get_db_session():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@router.get("/", response_model=List[schemas.Profile])
def list_profiles(db: Session = Depends(get_db_session)):
    return db.query(models.Profile).all()
