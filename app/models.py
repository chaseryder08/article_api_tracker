from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    ticket_number = db.Column(db.String(50), nullable=False)
    created_by = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    published_date = db.Column(db.DateTime)
    stage = db.Column(db.String(50), default="Draft")
    delay_reason = db.Column(db.Text)
    days_to_publish = db.Column(db.Integer)
