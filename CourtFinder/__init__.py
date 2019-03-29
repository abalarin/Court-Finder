from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from CourtFinder.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    # Init app contenxts
    db.init_app(app)

    from CourtFinder.endpoints.main.routes import main
    from CourtFinder.endpoints.courts.routes import courts
    from CourtFinder.endpoints.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(courts)
    app.register_blueprint(users)

    return app
