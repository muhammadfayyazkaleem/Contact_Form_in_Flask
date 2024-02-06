from website import db 

class ContactInfo(db.Model):
    id_no = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    message = db.Column(db.String(10000))
