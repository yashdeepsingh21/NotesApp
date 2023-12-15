from marshmallow import validates, fields as base_fields, post_load, validate
from extensions import ma
from UserAuth.schema import UserAuthSchema
from UserAuth.models import UserAuth


class UserAuthsParameter(UserAuthSchema):
    user_name = base_fields.String(required=True, validate=validate.Length(min=2, max=255),
                                   error_messages={"required": "name is required"})
    email = base_fields.Email(required=True, validate=validate.Length(min=4, max=255))
    password = base_fields.String(required=True, validate=validate.Length(min=4, max=255),
                                  error_messages={"required": "password is required"})

    class Meta:
        pass

    @validates('email')
    def validate_email(self, data, **kwargs):
        if UserAuth.query.filter_by(email=data).first():
            raise base_fields.ValidationError('Email already exists')
