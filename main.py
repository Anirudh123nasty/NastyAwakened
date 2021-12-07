from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

from flask import render_template, request
from crud import app_crud
from __init__ import app
import requests
import time
import ssl
import urllib.request, json
ssl._create_default_https_context = ssl._create_unverified_context

app.register_blueprint(app_crud)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("nasty.html")

@app.route('/michael/', methods=['GET', 'POST'])
def michael():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("michael.html", name=name)
    # starting and empty input default
    return render_template("michael.html", name="World")

@app.route('/anirudh/', methods=['GET', 'POST'])
def anirudh():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("anirudh.html", name=name)
    # starting and empty input default
    return render_template("anirudh.html", name="World", Img1="/static/assets/anirudhimages/anirudhmask.jpg", Img2="/static/assets/anirudhimages/anirudhnomask.jpg")

@app.route('/ethan/', methods=['GET', 'POST'])
def ethan():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("ethan.html", name=name)
            # starting and empty input default
    return render_template("ethan.html", name="World")


@app.route('/sahil/', methods=['GET', 'POST'])
def sahil():
    return render_template("sahil.html", pic1="/static/assets/sahilimages/sahilnomask.JPG", pic2="/static/assets/sahilimages/sahilmask.JPG")

@app.route('/nasty/')
def nasty():
    return render_template("nasty.html")

if __name__ == "__main__":
    app.run(debug=True)