# ===============================
# backend/app/schemas.py
# ===============================

from pydantic import BaseModel
from typing import Optional

# Auth / Device
class DeviceAuth(BaseModel):
    device_name: str
    device_type: str

# Profiles
class ProfileBase(BaseModel):
    name: str
    is_kids: bool
    max_rating_level: int

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    class Config:
        orm_mode = True

# Media
class MediaBase(BaseModel):
    title: str
    rating_level: int
    status: str

class Media(MediaBase):
    id: int
    primary_genre_id: int
    class Config:
        orm_mode = True
