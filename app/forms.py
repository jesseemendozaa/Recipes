from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, TextAreaField
from datetime import datetime

class RecipeForm(FlaskForm): # form for creating recipe
    title = StringField('Title', validators=[validators.DataRequired()])
    description = TextAreaField('Description', validators=[validators.DataRequired()]) 
    ingredients = TextAreaField('Ingredients', validators=[validators.DataRequired()])
    instructions = TextAreaField('Instructions', validators=[validators.DataRequired()])
    submit =  SubmitField("Create Recipe")
    remember_me = BooleanField("Remember Me")

class LoginForm(FlaskForm): # form for user login
    username = StringField('USERNAME', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=4, max=35)])
    remember_me = BooleanField("Remember Me")
    submit =  SubmitField("Log In")
