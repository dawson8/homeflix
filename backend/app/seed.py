from app.db import SessionLocal
from app.models import User, Profile, Genre, Media


def seed_database():
    db = SessionLocal()

    # ---- User ----
    user = db.query(User).first()
    if not user:
        user = User(
            email="admin@homeflix.local",
            password_hash="dev-placeholder"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        print("Seeded user")

    # ---- Profiles ----
    if db.query(Profile).count() == 0:
        profiles = [
            Profile(
                name="Admin",
                is_child=False,
                max_rating_level=18,
                user_id=user.id
            ),
            Profile(
                name="Kids",
                is_child=True,
                max_rating_level=7,
                user_id=user.id
            ),
        ]
        db.add_all(profiles)
        print("Seeded profiles")

    # ---- Genres ----
    if db.query(Genre).count() == 0:
        genres = [
            Genre(name="Animation", min_rating=0),
            Genre(name="Action", min_rating=12),
        ]
        db.add_all(genres)
        db.commit()
        print("Seeded genres")

    animation = db.query(Genre).filter_by(name="Animation").first()

    # ---- Media ----
    if db.query(Media).count() == 0:
        media_items = [
            Media(
                title="The Lion King",
                rating_level=0,
                status="approved",
                primary_genre_id=animation.id
            ),
            Media(
                title="Finding Nemo",
                rating_level=0,
                status="approved",
                primary_genre_id=animation.id
            ),
        ]
        db.add_all(media_items)
        print("Seeded media")

    db.commit()
    db.close()
