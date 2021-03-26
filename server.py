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

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    user_email = request.form('email')
    user_password = request.form('password')
    user = crud.get_user_by_email(user_email)

    if user:
        flash('This email already exists. Try again!')
    else:
        crud.create_user(user_email, user_password)
        flash('Account successfully created. You can now log in.')

    return redirect('/')

@app.route('/login', methods=['GET'])
def login_user():
    """Login user"""

    user_email = request.args.get('email')
    user_password = request.args.get('password')

    if session[user_email]:
        == user_password

    return redirect('/users/<user_id>')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
