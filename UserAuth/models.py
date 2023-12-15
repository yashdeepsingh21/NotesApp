from extensions import db
import datetime


class UserAuth(db.Model):
    __tablename__ = 'user_auth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, unique=True, autoincrement=True, default=0)
    user_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'id: {self.id}, user_name: {self.user_name}, email: {self.email}, password: {self.password}, created_at: {self.created_at}'
