from extensions import ma
from UserAuth.models import UserAuth


class UserAuthSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserAuth
        load_instance = True
        fields = (
            'user_id',
            'user_name',
            'email',
            "password",
        )
        dump_only = (
            'user_id',
        )
