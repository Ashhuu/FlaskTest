from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired


class SignUp(FlaskForm):
    name = StringField('Full Name:', [InputRequired()])
    email = StringField('Email', [Email(message='Not a valid email address.'), DataRequired()])
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirmPassword', message='Passwords must match')])
    confirmPassword = PasswordField('Repeat Password', [InputRequired()])
    submit = SubmitField('Submit')

class SignIn(FlaskForm):
    email = StringField('Email', [Email(message='Not a valid email address.'), DataRequired()])
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirmPassword', message='Passwords must match')])
