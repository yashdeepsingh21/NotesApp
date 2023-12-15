from flask import Flask
from extensions import db, api
from extensions import migrate, ma
from Notes.resources import notes, ns
from UserAuth.resources import user_auth


app = Flask(__name__)
api.init_app(app)
# from models.your_model import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://api_user:password@localhost/notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(notes)
app.register_blueprint(user_auth)

db.init_app(app)

api.add_namespace(ns)

migrate.init_app(app, db)
ma.init_app(app)
# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
