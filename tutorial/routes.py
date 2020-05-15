from flask import render_template, request
from tutorial import app
from tutorial import forms

@app.route('/')
def homePage():
    title = "My Website"
    description ="MY very own description"
    data = [{'name': 'Rahul', 'age': '15'}, {'name': 'Laxman', 'age': '16'}, {'name': 'Rohit', 'age': '15'}, {'name': 'Roy', 'age': '15'}]
    return render_template("homepage.html", title=title, description=description, data=data)


@app.route('/register', methods=["GET", "POST"])
def register():
    success = 0
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.form)
        print(request.form['name'])
        print(request.form['password'])
        print(request.form['email'])
        success = 1
    title = "Registration"
    description ="This is the registration page"
    return render_template("register.html", title=title, description=description, form=form, success=success)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.SignIn()
    if request.method == 'POST':
        form = forms.SignIn(request.form)

    title = "Registration"
    description ="This is the registration page"
    return render_template("register.html", title=title, description=description, form=form)