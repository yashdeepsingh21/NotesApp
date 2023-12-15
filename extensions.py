from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

api = Api()

migrate = Migrate()

ma = Marshmallow()
