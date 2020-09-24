from flask import Flask
from flask import request
from flask import abort, redirect, url_for

# python's calls programs' modules 
app = Flask(__name__)

#set FLASK_APP=main.py makes every program that runs can see


@app.route('/')
def index():
    return 'Index Page'

@app.route('/recipe')
def hello():
    return 'HongShaoRou is the best Rou'

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

