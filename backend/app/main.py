# ===============================
# backend/app/main.py
# ===============================

from fastapi import FastAPI
from app.routers import media, profiles, auth
from app.db import Base, engine

# Create all tables at startup (Phase-0, simple)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HomeFlix")

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
app.include_router(media.router, prefix="/media", tags=["media"])
