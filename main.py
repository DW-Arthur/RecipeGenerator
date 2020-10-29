from flask import Flask, request, abort, redirect, url_for, render_template
import requests
import json

api_key = "9105017d9e824e04a4c534ea357e2eba"
# python's calls programs' modules 
app = Flask(__name__)

#set FLASK_APP=main.py makes every program that runs can see

# login page
@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

    
@app.route('/')
def home():
    return render_template('home.html')


#Too many FB users (dynamic), %s is essentially printf
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'This is a post request'
    else:
        return 'This is a get request'

#template is a template that can be changed, templates is the blueprint that gets passed to javascript
#Jinja is the template for flask
#f is format string
#with will automatically close the file
# array of dictionaries
#requests allows you to pass dictionary called params, and param is dictionar, Weiran is a coding god, 
#This is for querries, the recipe instruction is not a querry request, therefore don't need a second param
@app.route('/recipe/')
def recipe():
    stuff = request.args.get('ingredients')
    data = requests.get('https://api.spoonacular.com/recipes/findByIngredients',params={"apiKey":api_key,"ingredients":stuff})
    recipe_data = json.loads(data.text)
    recipe_instructions =[]
    for i in recipe_data:
        instructions = requests.get(f'https://api.spoonacular.com/recipes/{i["id"]}/analyzedInstructions', params={"apiKey":api_key})
        recipe_instructions.append(json.loads(instructions.text))
    print(recipe_instructions)
    return render_template('recipe.html', recipes = recipe_data, instructions= recipe_instructions)


@app.route('/detail/')
def new():
    return render_template('detail.html')