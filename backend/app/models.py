# ===============================
# backend/app/models.py
# ===============================

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    devices = relationship("Device", back_populates="user")
    profiles = relationship("Profile", back_populates="user")

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    device_name = Column(String)
    device_type = Column(String)  # tv | mobile | web
    refresh_token_hash = Column(String)
    last_seen_at = Column(String)

    user = relationship("User", back_populates="devices")

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_child = Column(Boolean, default=True)
    max_rating_level = Column(Integer)
    pin_hash = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="profiles")

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    min_rating = Column(Integer)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    rating_level = Column(Integer)
    status = Column(String, default="pending_review")  # approved, pending_review, blocked
    primary_genre_id = Column(Integer, ForeignKey("genres.id"))

    primary_genre = relationship("Genre")
