"""
Developer utility to seed the database.

Run with:
python seed_db.py
"""

from app.db import engine
from app.models import Base
from app.seed import seed_database

if __name__ == "__main__":
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    # Seed data
    seed_database()
