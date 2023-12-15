from extensions import db
import datetime


class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    notes_id = db.Column(db.Integer, autoincrement=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_auth.user_id'), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    content = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'id: {self.id}, user_id: {self.user_id}, notes_id: {self.notes_id}, Title: {self.title}, Content: {self.content}, created_at: {self.created_at}, updated_at: {self.updated_at}'

