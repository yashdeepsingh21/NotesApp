from flask import Blueprint, request, jsonify
from flask_restx import Resource, Namespace
from Notes.models import Notes
from extensions import db, api
from Notes.parameter import UserNotesParameter, UpdateNotesParameter
from Notes.schema import NotesSchema
import datetime

user_param = UserNotesParameter()
note_schema = NotesSchema(many=True)
update_param = UpdateNotesParameter()

notes = Blueprint('notes', __name__)
ns = Namespace('notes', description='This is for Notes description')
api.add_namespace(ns)


@ns.route('/<int:user_id>')
class UserNotes(Resource):
    # @ns.response(NotesSchema(many=True), description='List of Notes')
    def get(self, user_id):
        try:
            data = Notes.query.filter_by(user_id=user_id).all()
            return note_schema.dump(data)
        except Exception as e:
            return {"message": str(e)}

    def post(self, user_id):
        try:
            data = user_param.load(request.json)
            notes_id = Notes.query.order_by(Notes.notes_id.desc()).first().notes_id
            id = Notes.query.order_by(Notes.id.desc()).first().id
            add_data = Notes(**data, notes_id=notes_id + 1, created_at = datetime.datetime.utcnow(), user_id = user_id, id = id + 1)
            print(add_data)
            db.session.add(add_data)
            db.session.commit()
            return {"message": "data added successfully"}
        except Exception as e:
            return {"message": str(e)}


@ns.route('/<int:user_id>/<int:notes_id>')
class UserNotesById(Resource):
    def get(self, user_id, notes_id):
        try:
            data = Notes.query.filter_by(user_id=user_id, notes_id=notes_id)
            return note_schema.dump(data)
        except Exception as e:
            return {"message": str(e)}

    def put(self, user_id, notes_id):
        try:
            data = Notes.query.get_or_404(notes_id)
            print(data)
            if data:
                add_data = update_param.load(request.json, instance=data)
                data.title = add_data.get("title", data.title)
                data.content = add_data.get("content", data.content)
                data.updated_at = datetime.datetime.utcnow()
                db.session.commit()
            return {"message": "data updated successfully"}
        except Exception as e:
            return {"message": str(e)}

    def delete(self, user_id, notes_id):
        try:
            data = Notes.query.get_or_404(notes_id)
            if data:
                db.session.delete(data)
                db.session.commit()
            return {"message": "data deleted successfully"}
        except Exception as e:
            return {"message": str(e)}
