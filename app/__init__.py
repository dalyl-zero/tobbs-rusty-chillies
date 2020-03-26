from flask import Flask
from flask_sqlalchemy import SQLAlchemy

root = '/chilli/variants'

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xe8\xaf\xa8\x00\x94^\x1e\x84\\)\xfc\x8d1\xbfN\x8c\x94D&\xdf\x1e\x0f\x1bg\xf0\x98L}2\xb03~'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/chilli'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    from . import routes
