from flask_sqlalchemy import SQLAlchemy
from .. import db

class Sample(db.Model):
    __tablename__ = 'samples'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sample_data = db.Column(db.String(255))