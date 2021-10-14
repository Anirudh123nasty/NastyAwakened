# import "packages" from flask
import requests
from flask import Flask, render_template, request
from algorithms.image import drawhack, michael_image_data, anirudh_image_data, \
    ethan_image_data, james_image_data, size_hack


# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("planner.html")

@app.route('/README/')
def README():
    return render_template("README.html")

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
    return render_template("anirudh.html", name="World")

@app.route('/ethan/', methods=['GET', 'POST'])
def ethan():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("ethan.html", name=name)
            # starting and empty input default
    return render_template("ethan.html", name="World")

@app.route('/james/', methods=['GET', 'POST'])
def james():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("james.html", name=name)
    # starting and empty input default
    return render_template("james.html", name="World")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    try:
        if request.form:
            bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary.html", bits=int(bits), staticOn="/static/assets/bulb_on.gif", staticOff="/static/assets/bulb_off.png")
    #if request.form:
     #   static = request.form.get("img")
    # starting and empty input default
    except:
        return render_template("binary.html", bits=8, staticOn="/static/assets/bulb_on.gif", staticOff="/static/assets/bulb_off.png")
    return render_template("binary.html", bits=8, staticOn="/static/assets/bulb_on.gif", staticOff="/static/assets/bulb_off.png")

@app.route('/binary2/', methods=['GET', 'POST'])
def binary2():
    try:
        if request.form:
            bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary2.html", bits=int(bits), staticOn2="/static/assets/bulb_on2.gif", staticOff2="/static/assets/bulb_off2.png")
    #if request.form:
    #   static = request.form.get("img")
    # starting and empty input default
    except:
        return render_template("binary2.html", bits=8, staticOn2="/static/assets/bulb_on2.gif", staticOff2="/static/assets/bulb_off2.png")
    return render_template("binary2.html", bits=8, staticOn2="/static/assets/bulb_on2.gif", staticOff2="/static/assets/bulb_off2.png")

@app.route('/binary3/', methods=['GET', 'POST'])
def binary3():
    try:
        if request.form:
            bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary3.html", bits=int(bits), staticOn="/static/assets/bulb_on.gif", staticOff="/static/assets/bulb_off.png")
    #if request.form:
    #   static = request.form.get("img")
    # starting and empty input default
    except:
        return render_template("binary3.html", bits=8, staticOn="/static/assets/bulb_on.gif", staticOff="/static/assets/bulb_off.png")
    return render_template("binary3.html", bits=8, staticOn="/static/assets/bulb_on.gif", staticOff="/static/assets/bulb_off.png")

@app.route('/binary4/', methods=['GET', 'POST'])
def binary4():
    try:
        if request.form:
            bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binary4.html", bits=int(bits), staticOn="/static/assets/bulb_onU.gif", staticOff="/static/assets/bulb_offU.png")
    #if request.form:
    #   static = request.form.get("img")
    # starting and empty input default
    except:
        return render_template("binary4.html", bits=8, staticOn="/static/assets/bulb_onU.gif", staticOff="/static/assets/bulb_offU.png")
    return render_template("binary4.html", bits=8, staticOn="/static/assets/bulb_onU.gif", staticOff="/static/assets/bulb_offU.png")

#@app.route('/binary2/', methods=['GET', 'POST'])
#def binary2():
    # if request.form:
    # bits = request.form.get("pets")
    #  if len(bits) != 0:  # input field has content
#  return render_template("binary2.html", pets=(bits))
    # starting and empty input default
  #  return render_template("binary2.html", bits=8)
#what does the code above do^?

@app.route('/nasty/')
def nasty():
    return render_template("nasty.html")

@app.route('/planner/')
def planner():
    return render_template("planner.html")

@app.route('/binarywithcat/', methods=['GET', 'POST'])
def binarywithcat():
    try:
        if request.form:
            bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binarywithcat.html", bits=int(bits), CatOn="/static/assets/caton.jpg", CatOff="/static/assets/catoff.jpg")
    #if request.form:
    #   static = request.form.get("img")
    # starting and empty input default
    except:
        return render_template("binarywithcat.html", bits=8, CatOn="/static/assets/caton.jpg", CatOff="/static/assets/catoff.jpg")
    return render_template("binarywithcat.html", bits=8, CatOn="/static/assets/caton.jpg", CatOff="/static/assets/catoff.jpg")


@app.route('/binarywithdog/', methods=['GET', 'POST'])
def binarywithdog():
    try:
        if request.form:
            bits = request.form.get("bits")
        if len(bits) != 0:  # input field has content
            return render_template("binarywithdog.html", bits=int(bits), DogOn="/static/assets/dogon.jpg", DogOff="/static/assets/dogoff.jpg")
    #if request.form:
    #   static = request.form.get("img")
    # starting and empty input default
    except:
        return render_template("binarywithdog.html", bits=8, DogOn="/static/assets/dogon.jpg", DogOff="/static/assets/dogoff.jpg")
    return render_template("binarywithdog.html", bits=8, DogOn="/static/assets/dogon.jpg", DogOff="/static/assets/dogoff.jpg")


# @app.route('/rgb/')
# def rgb():
#     return render_template("rgb.html")


@app.route('/michaelrgb/', methods=['GET', 'POST'])
def michaelrgb():
    char = michael_image_data()
    draw = drawhack()
    colorList = []
    grayList = []
    for img in char:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])
    try:
        if request.form:
            option = request.form["option"]
        if option == 'yes':
            return render_template("michaelrgb.html", images=draw)
        elif option == 'no':
            return render_template("michaelrgb.html", images=char, colored=colorList, grayed=grayList)
        else:
            return render_template("michaelrgb.html", images=char, colored=colorList, grayed=grayList)
    except:
        return render_template("michaelrgb.html", images=char, colored=colorList, grayed=grayList)

@app.route('/anirudhrgb/', methods=['GET', 'POST'])
def anirudhrgb():
    junk = anirudh_image_data()
    return render_template("anirudhrgb.html", images=junk )

@app.route('/jamesrgb/', methods=['GET', 'POST'])
def jamesrgb():
    trash = james_image_data()
    colorList = []
    grayList = []  # pass in the lists from the image_data() function
    for img in trash:
         colorList.append(img['base64'])
         grayList.append(img['base64_GRAY'])
    return render_template("jamesrgb.html", images=trash, colored=colorList, grayed=grayList )



@app.route('/ethanrgb/', methods=['GET', 'POST'])
def ethanrgb():
    mine = ethan_image_data()
    size = size_hack()
    try:
        if request.form:
            option = request.form["option"]
        if option == 'yes':
            return render_template("ethanrgb.html", images=size)
        elif option == 'no':
            return render_template("ethanrgb.html", images=mine)
        else:
            return render_template("ethanrgb.html", images=mine)
    except:
        return render_template("ethanrgb.html", images=mine)


@app.route('/colorcode2/')
def colorcode2():
    return render_template("colorcode2.html")

@app.route('/logicgate/', methods=['GET', 'POST'])
def logic():
    return render_template("logicgate.html")


@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("jokes.html", jokes=response.json())


@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("covid19.html", stats=response.json())

if __name__ == "__main__":
    app.run(debug=True)
