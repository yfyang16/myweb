# coding = utf-8
# Yufeng Yang

from flask import render_template, request, redirect, url_for, flash
from . import code


__author__ = 'Yufeng Yang'


@code.route('/code', methods=['GET'])
def show_pj():
    return render_template('pj.html')


