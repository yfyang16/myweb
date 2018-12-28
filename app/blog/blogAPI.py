# coding = utf-8
# Yufeng Yang

from flask import render_template, request, redirect, url_for, flash, jsonify, make_response

from app.forms.query_validation import SearchForm, is_id_validated
from . import blog
from app.models.blog_server import db
import time
import datetime

__author__ = 'Yufeng Yang'


@blog.route('/blog', methods=['GET'])
def show_bloglist():
    return render_template('tobedone.html')


@blog.route('/blog/list', methods=['GET'])
def get_list():

    form = SearchForm(request.args)
    if form.validate():
        start = form.start.data
    else:
        return "", 404
    all_lists = db.get_all_posts()
    if all_lists == -1:
        return "", 404
    all_lists.sort(key=lambda x: x[1])
    start_index = 0

    for i in range(len(all_lists)):
        if all_lists[i][1] == start:
            start_index = i

    all_lists = all_lists[start_index:]
    # header = {'Content-Type': 'application/json'}
    return render_template("blog_list.html", all_lists=all_lists)


@blog.route('/blog/list/<postid>', methods=['GET'])
def get_post(postid):

    if is_id_validated(postid) and postid!=0:
        particular_post = db.get_one_post(postid)
        if particular_post:
            header = {'Content-Type': 'application/json'}
            return jsonify(particular_post), 200, header
        else:
            return "", 403
    elif postid == 0:
        new_id = db.get_max_id() + 1
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        db.create_new_post(new_id, timestamp)

    elif int(postid) < 0:
        return "", 403
    else:
        return "", 404



