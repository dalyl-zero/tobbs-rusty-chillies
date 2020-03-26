from flask import Flask
from flask_sqlalchemy import SQLAlchemy

root = '/chilli/variants'

app = Flask(__name__)

# TODO: Refactor into secure config module
app.config['SECRET_KEY'] = b'\xe8\xaf\xa8\x00\x94^\x1e\x84\\)\xfc\x8d1\xbfN\x8c\x94D&\xdf\x1e\x0f\x1bg\xf0\x98L}2\xb03~'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gkavsdyobmlxmu' \
                                        ':1ef0e1353052b162493f9474219206e3497e5dc00e39d03357e67bbcab6dfbc2@ec2-54-147' \
                                        '-209-121.compute-1.amazonaws.com:5432/da6h54vq2btchh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

    from . import routes
