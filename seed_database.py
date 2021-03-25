"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']
    date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    db_movie = crud.create_movie(title, overview, date, poster_path)
    movies_in_db.append(db_movie)


for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    db_user = crud.create_user(email, password)

    for m in range(10):
        rated_movie = choice(movies_in_db)
        rated_score = randint(1, 5)

        crud.create_rating(db_user, rated_movie, rated_score)

# More code will go here