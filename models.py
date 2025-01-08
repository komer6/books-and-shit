from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()  # Initialize Bcrypt



# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # User ID
    username = db.Column(db.String(50), unique=True, nullable=False)  # Username
    password = db.Column(db.String(100), nullable=False)  # Hashed password
    email = db.Column(db.String(100), nullable=True)  # Email

    def __init__(self, username, password, email=None, bcrypt=None):
        self.username = username
        if bcrypt:  # Pass Bcrypt instance
            self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.email = email

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incremented ID
    name = db.Column(db.String(100), nullable=False)  # Book name
    author = db.Column(db.String(100), nullable=False)  # Author name
    genre = db.Column(db.String(50), nullable=False)  # Genre
    year = db.Column(db.Integer, nullable=False)  # Year of publication
    amount = db.Column(db.Integer, nullable=False)  # Amount of books in stock
    loandate = db.Column(db.Integer, nullable=False)  # Number of loan days available
    image = db.Column(db.String(100), nullable=False)  # Path to the book image

    def __repr__(self):
        return f"<Book {self.name} by {self.author}>"
