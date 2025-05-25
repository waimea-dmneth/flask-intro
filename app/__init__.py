from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from random import randint

app = Flask(__name__)

# Home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# About page - loading a static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# Random number page - passing a random int value into the template
@app.get("/random/")
def random():
    randNum = randint(1,500000)
    return render_template('pages/random.jinja', number = randNum)

# Number Page - getting a value from the root and passing it into template
@app.get("/number/<int:num>")
def analyseNum(num):
    return render_template('pages/number.jinja', number = num)

# Form Page - Static page with a form
@app.get("/form/")
def form():
    return render_template('pages/form.jinja')

# Handle data posted from the form
@app.post("/processForm")
def processForm():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/formData.jinja",
        ccn = request.form["ccn"],
        ssn = request.form["ssn"]
    )    

# Missing Page error - redirects to homepage
@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja/")