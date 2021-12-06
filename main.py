from flask import Flask, render_template, request
import urllib.request, json
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

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
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"San Diego","lat":"32.7157","lon":"-117.161087","id":"2172797","lang":"null","units":"imperial","mode":"json"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "e2d0d1a7efmsh5668be741c711ffp1a3e44jsnfc9e0a91c2b2"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    mydict = json.loads(response.text)
    print(mydict)
    return render_template("anirudh.html", name="World", Img1="/static/assets/anirudhimages/anirudhmask.jpg", Img2="/static/assets/anirudhimages/anirudhnomask.jpg", myweather=mydict )

@app.route('/ethan/', methods=['GET', 'POST'])
def ethan():
    if request.form:
        word = request.form.get("word")
        with urllib.request.urlopen(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}") as url:
            data = json.loads(url.read().decode())
            definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        return render_template("ethan.html", word=word, mydef=definition)
    return render_template("ethan.html", word="Word appears here", mydef="Definition here")
    # word = request.form.get("word")
    # if word is None:
    #     return render_template("ethan.html", mydef="Definition here")
    # else:
    #     with urllib.request.urlopen(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}") as url:
    #         data = json.loads(url.read().decode())
    #         definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    #     return render_template("ethan.html", mydef=definition)
        # if len(word) != 0:
        #     with urllib.request.urlopen(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}") as url:
        #         data = json.loads(url.read().decode())
        #         definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        # return render_template("ethan.html", mydef=definition)
        #     # starting and empty input default



    # return render_template("ethan.html", mydef="Definition here")


@app.route('/sahil/', methods=['GET', 'POST'])
def sahil():
    url = "https://best-booking-com-hotel.p.rapidapi.com/booking/best-accommodation"

    querystring = {"cityName":"San Diego","countryName":"United States"}

    headers = {
        'x-rapidapi-host': "best-booking-com-hotel.p.rapidapi.com",
        'x-rapidapi-key': "df17610e35msh51d75ac58fb44f9p14c5f0jsn7d95a150e08b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    dict = json.loads(response.text)
    return render_template("sahil.html", pic1="/static/assets/sahilimages/sahilnomask.JPG", pic2="/static/assets/sahilimages/sahilmask.JPG", myHotel=dict)

@app.route('/byron/')
def byron():
    return render_template("byron.html")

@app.route('/nasty/')
def nasty():
    return render_template("nasty.html")


@app.route('/sports/')
def sports():
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    querystring = {"Category":"soccer"}

    headers = {
        'x-rapidapi-host': "livescore6.p.rapidapi.com",
        'x-rapidapi-key': "e919089b4amsh0b802c611d0362cp1ef95cjsn19265aeec315"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return render_template("sports.html")

if __name__ == "__main__":
    app.run(debug=True)
