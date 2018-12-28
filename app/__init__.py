# coding=utf-8
# Yufeng Yang


from flask import Flask


__author__ = 'Yufeng Yang'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    register_blueprint(app)

    return app


def register_blueprint(app):
    from app.cv import cv
    from app.blog import blog
    from app.code import code
    app.register_blueprint(cv)
    app.register_blueprint(blog)
    app.register_blueprint(code)

