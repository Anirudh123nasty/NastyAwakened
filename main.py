from flask import render_template, request
from crud import app_crud
from __init__ import app
import json
import requests
import time


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
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": "San Diego", "days": "30"}
    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "7f40b4d84bmsha2a68aaf4baa0afp168062jsncc2e438f86de"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    mydict = json.loads(response.text)
    print(mydict)
    return render_template("anirudh.html", name="World", Img1="/static/assets/anirudhimages/anirudhmask.jpg",
                           Img2="/static/assets/anirudhimages/anirudhnomask.jpg", myforecast=mydict)


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
    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"

    cities = ["San Diego", "Los Angeles", "New York", "Lincoln", "Miami"]
    for city in cities:
        querystring = {"cityName": city, "countryName": "United States"}

        headers = {
            'x-rapidapi-host': "best-booking-com-hotel.p.rapidapi.com",
            'x-rapidapi-key': "df17610e35msh51d75ac58fb44f9p14c5f0jsn7d95a150e08b"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        time.sleep(5)

    print(response.text)
    dict = json.loads(response.text)
    return render_template("sahil.html", pic1="/static/assets/sahilimages/sahilnomask.JPG",
                           pic2="/static/assets/sahilimages/sahilmask.JPG", myHotel=dict)


@app.route('/nasty/')
def nasty():
    return render_template("nasty.html")


if __name__ == "__main__":
    app.run(debug=True)
