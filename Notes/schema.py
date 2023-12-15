from extensions import ma
from Notes.models import Notes


class NotesSchema(ma.SQLAlchemyAutoSchema):
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
