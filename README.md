## SETUP INSTRUCTIONS:

(Please run following commands 1 at a time in your terminal (Lines starting with # are comments)) 

git clone https://github.com/jesseemendozaa/Recipes.git

cd Recipes

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

#Now we create the data base

flask shell

from app import db, myapp_obj

from app.models import Recipe, User

db.create_all()

exit()

#Now we can run our program

python3 run.py

## You should now be able to navigate to http://127.0.0.1:5000/recipe/new to start creating recipes!

#To leave the venv, please enter following command into terminal:

deactivate
