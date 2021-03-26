"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

@app.route('/')
def homepage():
    """See homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def view_movies():
    """See all movies"""
    
    movies = crud.all_movies()
    return render_template('all_movies.html', see_movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show movie details"""

    movie = crud.get_movie_by_id(movie_id)
    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def show_users():
    """Show all users"""

    users = crud.all_users()
    return render_template('all_users.html', see_users=users)


@app.route('/users/<user_id>')
def see_user(user_id):
    """Show user profile"""

    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)

    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
