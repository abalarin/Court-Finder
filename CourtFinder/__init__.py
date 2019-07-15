from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

from CourtFinder.config import Config
from CourtFinder.s3config.configer import getConfig
from CourtFinder.s3config.authBoto import botoClient, botoResource

config = getConfig(Config.APP_ROOT + '/s3config/config.ini')
client = botoClient(Config.BOTO_KEY, Config.BOTO_SECRET, config['object_api']['base_url'], config['object_api']['user'])
resource = botoResource(Config.BOTO_KEY, Config.BOTO_SECRET, config['object_api']['base_url'], config['object_api']['user'])

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    # Init app contenxts
    db.init_app(app)
    ma.init_app(app)

    # Init Login LoginManager
    from CourtFinder.models.users import load_user
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    from CourtFinder.endpoints.main.routes import main
    from CourtFinder.endpoints.courts.routes import courts
    from CourtFinder.endpoints.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(courts)
    app.register_blueprint(users)

    return app
