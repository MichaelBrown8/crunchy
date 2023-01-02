from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

# def passwords_match(form, field):
#     password = field.data
#     repeatPassword = field.data
#     if password != repeatPassword:
#         raise ValidationError('Passwords must match.')


class SignUpForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), user_exists])
    username = StringField(
        'username', validators=[DataRequired(), username_exists])
    firstName = StringField('first_name', validators=[DataRequired()])
    lastName = StringField('last_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    # repeatPassword = StringField('repeat password', validators=[DataRequired()])
