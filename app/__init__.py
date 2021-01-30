from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pathlib


basedir = pathlib.Path().absolute()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)


from app import models
from app import views
from app import urls


db.create_all()