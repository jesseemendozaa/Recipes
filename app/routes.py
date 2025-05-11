from ctypes import resize
from app import myapp_obj
from flask import render_template
from flask import redirect
from flask import Flask, request # Added flask and request
from flask_sqlalchemy import SQLAlchemy # Added SQLAlchemy
from app.forms import RecipeForm, LoginForm
from app.models import Recipe, User # importing from models.py
from app import db
from datetime import datetime # added datetime
# from <X> import <Y>

# Please check the README.md file for setup instructions

@myapp_obj.route("/") # http://127.0.0.1:5000/
def main():
    recipe = Recipe.query.all() # get all recipes
    return render_template("hello.html", recipe=recipe)

@myapp_obj.route("/recipe/new", methods=['GET', 'POST']) # http://127.0.0.1:5000/recipe/new
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        #create recipe
        new_recipe = Recipe(title=form.title.data, description=form.description.data, ingredients=form.ingredients.data, instructions=form.instructions.data, date=datetime.now())
        db.session.add(new_recipe) #adding to database
        db.session.commit()
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("new.html", form=form) #recipe form

@myapp_obj.route("/recipe/<int:integer>") # http://127.0.0.1:5000/recipe/<enter number here>
def return_recipe(integer):
    recipe = Recipe.query.get(integer) # get recipe number
    if recipe is None:
        print("Recipe not found") #prints to terminal
        return ""
    return render_template("return_rec.html", recipe=recipe)

@myapp_obj.route("/recipe/<int:integer>/delete") # http://127.0.0.1:5000/recipe/<enter number here>/delete
def delete_recipe(integer):
    del_rec = Recipe.query.get(integer) # get recipe number
    db.session.delete(del_rec) #delete
    db.session.commit()

    return f"Recipe deleted: {integer}"