from flask import Flask


def create_api():
    # create and configure api
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # import blueprints
    from Mydiary.templates import index
    from Mydiary.templates import diary_app

    # register blueprints
    app.register_blueprint(index)
    app.register_blueprint(diary_app)

    return app