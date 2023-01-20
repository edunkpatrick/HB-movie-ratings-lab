"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db, db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

app = Flask(__name__)


# Replace this with routes and view functions!
# create homepage
@app.route('/')
def homepage():
    """Homepage"""

    return render_template('homepage.html', )

@app.route('/movies')
def view_movies():
    """List of movies"""
    movies = crud.get_all_movies()

    return render_template('view_movies.html', movies=movies)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details of a movie"""
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route("/users")
def view_users():

    users = crud.create_user_list()

    return render_template('view_users.html', users=users)

@app.route("/user/<user_id>")
def show_user(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
