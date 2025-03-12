from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import login_manager
from app import db  # ✅ db импортируется из app/__init__.py

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    clicks = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'User {self.username} - clicks: {self.clicks}'





@login_manager.user_loader # Этот декоратор связывает функцию с flask_login, чтобы загружать пользователя по id
def load_user(user_id):
    return User.query.get(int(user_id))
