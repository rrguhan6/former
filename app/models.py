from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Book = db.Column(db.String(80), unique=True, nullable=False)
    Author = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.username