"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# CRUD Functions
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, 
                    release_date=release_date, 
                    poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


if __name__ == '__main__':
    from server import app
    connect_to_db(app)