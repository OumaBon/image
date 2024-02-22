from flask_sqlalchemy import SQLAlchemy
from main import app

db=SQLAlchemy(app)

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
    def create_user():
        new_user= User(name="Joan",password="1234")
        db.session.add(new_user)
        db.session.commit()

    
