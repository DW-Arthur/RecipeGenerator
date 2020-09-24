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

@app.route('/login2', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

#Similar to google search, might not need this
searchword = request.args.get('q', '')@app.route('/')

#Recipe


