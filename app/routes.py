from turtle import title
from flask import redirect, render_template, url_for, flash, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
#decorator to make sure a user is logged in before accessing this page
@login_required
def index():
    # locations =  [
    #     {
    #         'place': {'name': 'Greensfield'},
    #         'description' : 'Countryside with green hills and beautiful valleys'
    #     },
    #     {
    #         'place' : {'name': 'Meadows'},
    #         'description' : 'The meadows by the riverside'
    #     }
    # ]
    return render_template('index.html', title='Home')
#login route
@app.route('/login', methods=['GET', 'POST'])


#login function
def login():
    #check if a user is authenticated
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    #create a new object of LoginForm
    form = LoginForm()

    #validate form contents
    if form.validate_on_submit():
        #check the database for the user
        user = User.query.filter_by(username=form.username.data).first()
        #if user is non-existent or the password provided is wrong
        if user is None or not user.get_password(form.password.data):
            #alert the user and redirect to login
            flash('Invalid username or password')
            return redirect(url_for('login'))
        #if credentials are correct log in the user
        login_user(user, remember=form.remember_me.data)
        #redirect to the page the user was trying to access (stored in next)
        next_page = request.args.get('next')
        #if the 'next' is blank
        if not next_page or url_parse(next_page).netloc != '':
            #set next_page to the index page
            next_page = url_for('index')
        #redirect here
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
#logout function
def logout():
    logout_user()
    return redirect(url_for('index'))

#register view function
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations! You are now a registered user')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
