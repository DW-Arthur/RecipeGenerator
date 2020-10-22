from flask import Flask, request, abort, redirect, url_for, render_template


# python's calls programs' modules 
app = Flask(__name__)

#set FLASK_APP=main.py makes every program that runs can see


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
@app.route('/recipe/')
def test():

    return render_template('recipe.html', recipes = ["apple", "banana", "chicken"])