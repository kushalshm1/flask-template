from flask import render_template, request, Blueprint
management = Blueprint('management',__name__)

@management.route("/")
@management.route("/home")
def home():
    return render_template('home.html')
