"""Crud operations."""

from model import db, User, Movie, Rating, connect_to_db

# Functions start here


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_user_list():
    # returns a list of users
    return User.query.all()

def get_user_by_id(user_id):
    # returns a user
    return User.query.get(user_id) 
    
def create_movie(title, overview, release_date, poster_path):

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie

def get_all_movies():
    # returns all movies
    return Movie.query.all()

def get_movie_by_id(movie_id):
    # returns a movie by id
    return Movie.query.get(movie_id)

def create_rating(user, movie, score):

    rating = Rating(user=user, movie=movie, score=score)

    return rating
def get_user_by_email(email):
    """Return a user by email"""
    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)