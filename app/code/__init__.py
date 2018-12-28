# coding=utf-8
# Yufeng Yang

from flask import Blueprint
# from flask import render_template

__author__ = 'Yufeng Yang'

code = Blueprint('code', __name__)


from app.code import code_control