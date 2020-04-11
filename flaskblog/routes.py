from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post
from flaskblog import app

posts = [
    {
        'author': 'Keshav Mishra',
        'title' : 'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 11, 2020'
    },
    {
        'author': 'Avinash Mishra',
        'title' : 'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 12, 2020'
    },
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title = 'Home Page')


@app.route("/about")
def about():
    return render_template('about.html',title = 'About Page')


@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "mishrakeshav@gmail.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect('home')
        else:
            flash("Login Unsuccessful! Please Check Email and Password", "danger")
            
    return render_template('login.html',title = 'Login', form = form)

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}","success")
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register', form = form)
