from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/psudeonym')
def psudeonym():
    return render_template("psudeonym.html")
    
@app.route('/thanksSub', methods = ["GET", "POST"])
def thanksSub():
    if request.method == 'GET':
        return "Login Now."
    else:
        userData = dict(request.form)
        userName = userData['userName']
        if userName.lower() == "crazy dreamer":
            return render_template("sydney.html")
        elif userName.lower() == "joker":
            return render_template("patrick.html")
        elif userName.lower() == "yawn":
            return render_template("derek.html")
        elif userName.lower() == "lucky prophet":
            return render_template("kelsey.html")
        elif userName.lower() == "red one":
            return render_template("luke.html")
        elif userName.lower() == "two times two":
            return render_template("neydeli.html")
        elif userName.lower() == "cantonese":
            return render_template("lexi.html")
        return render_template("thanksSub.html", userName = userName)


        # userName = userData['userName']
        # if userName.lower() == "sydney":
        #     return render_template("sydney.html")
        # elif userName.lower() == "patrick":
        #     return render_template("patrick.html")
        # elif userName.lower() == "derek":
        #     return render_template("derek.html")
        # elif userName.lower() == "kelsey":
        #     return render_template("kelsey.html")
        # elif userName.lower() == "luke":
        #     return render_template("luke.html")
        # elif userName.lower() == "neydeli":
        #     return render_template("neydeli.html")
        # elif userName.lower() == "lexi":
        #     return render_template("lexi.html")
        # return render_template("thanksSub.html", userName = userName)
        #does it work?
