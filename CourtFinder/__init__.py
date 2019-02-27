from flask import Flask


def create_app():
    app = Flask(__name__)

    from CourtFinder.endpoints.main.routes import main
    from CourtFinder.endpoints.courts.routes import courts
    from CourtFinder.endpoints.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(courts)
    app.register_blueprint(users)

    return app
