# Yufeng Yang

from flask import render_template, request, redirect, url_for, flash
from . import cv


__author__ = 'Yufeng Yang'


@cv.route('/cv', methods=['GET', 'POST'])
def show_cv():
    return render_template('cv.html')


