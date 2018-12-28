# coding=utf-8
# Yufeng Yang

from wtforms import Form, StringField, IntegerField
from wtforms.validators import NumberRange

from app.forms.form_config import POSTIDMAX


class SearchForm(Form):
    # start = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    start = IntegerField(validators=[NumberRange(min=1, max=POSTIDMAX)], default=1)


def is_id_validated(postid):

    return 0 <= int(postid) <= POSTIDMAX
