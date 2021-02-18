from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask import flash

from flask_login import current_user
from impact.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'confirm_password', message="Please make sure your passwords match!")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Create Account")
    
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email is already in use!")

    def check_username(self, field):
        if User.query.filer_by(username=field.data).first():
            flash('Username is already taken!')
            raise ValidationError("Username is already taken!")


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    avatar = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
