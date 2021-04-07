from flask import Flask, render_template

app = Flask(__name__)


# creating an app instance
# use a decorator @ to define the route for our web page
@app.route("/")
# setting up a default page
def index():
    return "Welcome to DevOps team"


@app.route("/welcome/")
def welcome():
    return f"Welcome on board"


@app.route("/home/")
def home():
    return render_template("index.html")


@app.route("/register/")
def register():
    return render_template("register.html")


@app.route("/login/")
def login():
    return render_template("login.html")
