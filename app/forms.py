from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class userForm(Form):
    # DataRequired() doesn't allow empty Fields
    name = TextField('name',validators=[DataRequired()])
    phone = TextField('phone',validators=[DataRequired()])
    


