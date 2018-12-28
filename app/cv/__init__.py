# Yufeng Yang

from flask import Blueprint
# from flask import render_template

__author__ = 'Yufeng Yang'

cv = Blueprint('cv', __name__)


# @web.app_errorhandler(404)
# def not_found(e):
#     return render_template('404.html'), 404


from app.cv import cv_control

