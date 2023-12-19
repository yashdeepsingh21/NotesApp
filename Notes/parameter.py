from marshmallow import validates, fields as base_fields, post_load, validate, Schema
from Notes.schema import NotesSchema


class UserNotesParameter(Schema):
    title = base_fields.String(required=True, validate=validate.Length(min=2, max=255), attribute="title")
    content = base_fields.String(required=False, attribute="content")
    notes_id = base_fields.Integer(required=False, attribute="notes_id")


class UpdateNotesParameter(NotesSchema):
    title = base_fields.String(required=False)
    content = base_fields.String(required=False)

    class Meta:
        pass
