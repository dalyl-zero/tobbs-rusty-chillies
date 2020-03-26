from . import db


class ChilliVariant(db.Model):
    __tablename__ = 'variant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    scoville = db.Column(db.Integer, unique=False, nullable=False)
    days_to_germinate = db.Column(db.Integer, unique=False, nullable=False)
