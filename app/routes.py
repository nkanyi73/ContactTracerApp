from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nick'}
    locations =  [
        {
            'place': {'name': 'Greensfield'},
            'description' : 'Countryside with green hills and beautiful valleys'
        },
        {
            'place' : {'name': 'Meadows'},
            'description' : 'The meadows by the riverside'
        }
    ]
    return render_template('index.html', title='Home', user=user, locations=locations)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
