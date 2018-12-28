# coding=utf-8
# Yufeng Yang

from flask import Blueprint
# from flask import render_template

__author__ = 'Yufeng Yang'

blog = Blueprint('blog', __name__)


from app.blog import blogAPI