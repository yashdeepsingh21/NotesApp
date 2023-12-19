from extensions import ma
from Notes.models import Notes
from marshmallow import Schema


class NotesSchema(ma.SQLAlchemyAutoSchema, Schema):
    class Meta:
        model = Notes
        load_instance = True
        fields = (
            'notes_id',
            'user_id',
            'title',
            'content',
            'created_at',
            'updated_at',
        )
