# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# from apps.authentication.oauth import github_blueprint

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module

# ----------------------------------------
# my bp site
#
from apps.home.sample.app1 import bp as sample_app1
from apps.home.sample.app2 import bp as sample_app2
from apps.home.sample.app3 import bp as sample_app3
from apps.home.sample.app4 import bp as sample_app4
from apps.home.sample.app5 import bp as sample_app5
from apps.home.sample.app6 import bp as sample_app6
from apps.home.sample.app7 import bp as sample_app7
from apps.home.sample.app8 import bp as sample_app8
from apps.home.sample.app9 import bp as sample_app9
from apps.home.sample.app10 import bp as sample_app10
from apps.home.sample.app11 import bp as sample_app11
from apps.home.sample.app12 import bp as sample_app12
from apps.home.sample.app13 import bp as sample_app13

db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('authentication', 'home'):
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    from apps.authentication.oauth import github_blueprint
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)

    app.register_blueprint(github_blueprint, url_prefix="/login")
    register_blueprints(app)

    # regit sample site
    app.register_blueprint(sample_app1)
    app.register_blueprint(sample_app2)
    app.register_blueprint(sample_app3)
    app.register_blueprint(sample_app4)
    app.register_blueprint(sample_app5)
    app.register_blueprint(sample_app6)
    app.register_blueprint(sample_app7)
    app.register_blueprint(sample_app8)
    app.register_blueprint(sample_app9)
    app.register_blueprint(sample_app10)
    app.register_blueprint(sample_app11)
    app.register_blueprint(sample_app12)
    app.register_blueprint(sample_app13)

    configure_database(app)
    return app
