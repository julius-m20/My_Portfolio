from flask_wtf import form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class signIn(form):
    Name = StringField('Name', validators=[DataRequired("PLease Enter your Name.")])
    Password = PasswordField('Password', validators=[DataRequired("PLease Enter your Name.")])
    submit = SubmitField('signIn')