from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField,SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = TextAreaField('No. of Rooms', validators=[DataRequired()])
    bathrooms = TextAreaField('No. of Bathrooms', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])
    ptype = SelectField('Property Type', choices=[('House', 'House'), ('Apartment','Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['png','jpg'],"Only upload images.")])
