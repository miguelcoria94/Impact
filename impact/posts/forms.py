from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Body', validators=[DataRequired()])
    post_image = FileField('Choose Image', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    submit = SubmitField('Create Post')
