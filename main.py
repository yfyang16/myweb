# coding = utf-8
# Yufeng Yang

from flask import render_template
from app import create_app
from flask import redirect,url_for

__author__ = 'Yufeng Yang'

app = create_app()


@app.route('/',methods=['GET'])
def show_index():
    return render_template('index.html')
    # return redirect(url_for('web.book_detail', isbn=isbn))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)

