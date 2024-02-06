from website import db 
from flask_login import UserMixin

class ContactInfo(db.Model):
    id_no = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    message = db.Column(db.String(10000))

class User(db.Model, UserMixin):
    id_no = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.username}')"

    def get_id(self):
        return str(self.id_no)

