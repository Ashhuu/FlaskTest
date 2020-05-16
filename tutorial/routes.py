from flask import render_template, request, redirect
from tutorial import app, db
from tutorial import forms
from tutorial.models import User
from flask_login import current_user, login_user, logout_user

@app.route('/')
def homePage():
    isActive = 0
    if current_user.is_authenticated:
        isActive = 1
    title = "My Website"
    description ="MY very own description"
    data = [{'name': 'Rahul', 'age': '15'}, {'name': 'Laxman', 'age': '16'}, {'name': 'Rohit', 'age': '15'}, {'name': 'Roy', 'age': '15'}]
    return render_template("homepage.html", title=title, description=description, data=data, isActive=isActive)

@app.route('/register', methods=["GET", "POST"])
def register():
    isActive = 0
    if current_user.is_authenticated:
        isActive = 1
    success = 0
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.form)
        user = User(username=request.form['username'], email=request.form['email'])
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        success = 1
    title = "Registration"
    description ="This is the registration page"
    return render_template("register.html", title=title, description=description, form=form, success=success, isActive=isActive)

@app.route('/userdetails')
def userdetails():
    isActive = 0
    if current_user.is_authenticated:
        isActive = 1
    data = User.query.all()
    return render_template('userdetails.html', data=data, isActive=isActive)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/dashboard')
    form = forms.SignIn()
    isActive = 0
    if request.method == 'POST':
        form = forms.SignIn(request.form)
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None or not user.check_password(request.form['password']):
            return redirect('/login')
        login_user(user, remember=True)
        return redirect('/dashboard')
    title = "Welcome to Login"
    description ="You can login here"
    return render_template("login.html", title=title, description=description, form=form)

@app.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        return redirect('/login')
    isActive = 1
    title = "My Dashboard"
    description = "This is your logged in page"
    return render_template("dashboard.html", title=title, description=description, isActive=isActive)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')