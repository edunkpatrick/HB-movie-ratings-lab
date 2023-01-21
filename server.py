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

    return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def login_authentication():
    """Verifies user log in"""
    email = request.form.get("email")
    password = request.form.get("password")

    # check database for entered email
    # verify password stored with that email matches

    # users can have same password, search by email
    # authentication = crud.get_user_by_password(email)

    user = crud.get_user_by_email(email)

    if user:
        if user.password == password:
            session["email"] = email
        else:
            flash("Incorrect password")

    # if authentication:
    #     flash("Incorrect password")
    # else:
    #     session["email"] = email
    # flash("Logged in!")

    return redirect('/')

@app.route('/users', methods = ['POST'])
def create_user():
    """Create a user"""
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    # check if a user with the email from request.form already exists
    if user:
        flash("Account with that email exists, please try again.")
    # if user does not exist with that email, commit user to database
    else:
        user=crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully, please log in.")

    return redirect('/')

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
