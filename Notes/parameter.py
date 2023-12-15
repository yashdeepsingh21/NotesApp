from marshmallow import validates, fields as base_fields, post_load, validate
from Notes.schema import NotesSchema
from Notes.models import Notes


class UserNotesParameter(NotesSchema):
    title = base_fields.String(required=True, validate=validate.Length(min=2, max=255))
    content = base_fields.String(required=False)

    class Meta:
        model = Notes
        fields = (
            'title',
            'content',
        )


class UpdateNotesParameter(NotesSchema):
    title = base_fields.String(required=False)
    content = base_fields.String(required=False)

    class Meta:
        pass
