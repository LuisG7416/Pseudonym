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
        return render_template("thanksSub.html", userName = userName)
