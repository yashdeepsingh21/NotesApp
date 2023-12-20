from flask import Blueprint, request
from flask_restx import Resource, Namespace
from UserAuth.models import UserAuth
from extensions import db, api
from UserAuth.schema import UserAuthSchema
from UserAuth.parameter import UserAuthsParameter
from marshmallow import ValidationError

user_auth = Blueprint('user_auth', __name__)
ns = Namespace('user_auth', description='UserAuth operations')
api.add_namespace(ns)
user_auth_schema = UserAuthSchema(many=True)
user_auth_parameter = UserAuthsParameter()


@ns.route('/')
class UserAuths(Resource):

    @ns.response(UserAuthSchema(many=True), description='List of user_auths')
    def get(self):
        data = UserAuth.query.all()
        return {"users": user_auth_schema.dump(data)}

    @ns.response(UserAuthSchema(), description='UserAuth')
    @ns.expect(UserAuthsParameter())
    def post(self):
        try:
            data = user_auth_parameter.load(request.json)
            user_id = UserAuth.query.order_by(UserAuth.id.desc()).first().id
            add_data = UserAuth(**data, user_id=user_id + 1)
            db.session.add(add_data)
            db.session.commit()
            return {"message": "data added successfully"}
        except ValidationError as e:
            return {"message": str(e)}, 400  # Bad request error code}
        except Exception as e:
            return {"message": str(e)}


@ns.route('/<user_id>')
class UserAuthById(Resource):

    @api.response(UserAuthsParameter(), description='UserAuth')
    def get(self, user_id):
        try:
            data = UserAuth.query.get_or_404(user_id)
            dict = {data}
            return user_auth_schema.dump(dict)
        except Exception as e:
            return {"message": str(e)}

    # @api.expect(UserAuthsParameter())
    def put(self, user_id):
        try:
            data = UserAuth.query.get_or_404(user_id)
            if data:
                add_data = UserAuthsParameter(partial=True).load(request.json, instance=data)
                db.session.add(add_data)
                db.session.commit()
            return {"message": "data updated successfully"}
        except ValidationError as e:
            return {"message": str(e)}, 400  # Bad request error code
        except Exception as e:
            return {"message": str(e)}

    def delete(self, user_id):
        try:
            data = UserAuth.query.get_or_404(user_id)
            if data:
                db.session.delete(data)
                db.session.commit()
            return {"message": "data deleted successfully"}
        except Exception as e:
            return {"message": str(e)}

