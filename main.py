from flask import Flask, render_template, request
import json
import requests
# create a Flask instance
app = Flask(__name__)


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
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q":"San Diego","days":"30"}
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "7f40b4d84bmsha2a68aaf4baa0afp168062jsncc2e438f86de"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    mydict = json.loads(response.text)
    print(mydict)
    return render_template("anirudh.html", name="World", Img1="/static/assets/anirudhimages/anirudhmask.jpg", Img2="/static/assets/anirudhimages/anirudhnomask.jpg", myforecast=mydict )

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