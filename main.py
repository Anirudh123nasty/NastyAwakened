# import "packages" from flask
from flask import Flask, render_template, request
from algorithms.image import drawhack, michael_image_data, anirudh_image_data, ethan_image_data, james_image_data


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
    return render_template("michael.html", name="")

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


#@app.route('/binary2/', methods=['GET', 'POST'])
#def binary2():
    # if request.form:
    # bits = request.form.get("pets")
    #  if len(bits) != 0:  # input field has content
#  return render_template("binary2.html", pets=(bits))
    # starting and empty input default
  #  return render_template("binary2.html", bits=8)
#what does the code above do^?

@app.route('/About/')
def About():
    return render_template("About.html")

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
    try:
        if request.form:
            option = request.form["option"]
        if (option == 'yes'):
            return render_template("michaelrgb.html", images=draw)
        elif (option == 'no'):
            return render_template("michaelrgb.html", images=char)
    except:
        return render_template("michaelrgb.html", images=char)

@app.route('/anirudhrgb/', methods=['GET', 'POST'])
def anirudhrgb():
    junk = anirudh_image_data()
    return render_template("anirudhrgb.html", images=junk )

# add your own individual /namergb/ htmls with your own image_data for hacks

if __name__ == "__main__":
    app.run(debug=True)
