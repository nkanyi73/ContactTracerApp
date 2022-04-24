from enum import unique
from app import db, login
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin

#defining the user class
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #high-level view of the relationship between users and location
    locations = db.relationship('Location', backref='visitor', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    #loading a user for flask login
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

#defining the location class
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), index=True)
    #foreign key to the users table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #The __repr__ method tells Python how to print objects of this class
    def __repr__(self):
        return 'Location {}'.format(self.name)