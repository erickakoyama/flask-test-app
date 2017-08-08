from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired('Please enter your first name.')])
    last_name = StringField('Last name', validators=[DataRequired('Please enter your last name.')])
    email = StringField('Email', validators=[DataRequired('Please enter your email.'), Email('Please enter a valid email.')])
    password = PasswordField('Password', validators=[DataRequired('Please enter a password.'), Length(min=6, message="Please enter password equal to or longer than 6 characters")])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Please enter your email.'), Email('Please enter a valid email.')])
    password = PasswordField('Password', validators=[DataRequired('Please enter a password.')])
    submit = SubmitField('Login')
