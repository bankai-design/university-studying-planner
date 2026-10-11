from flask import Blueprint, render_template

mainBlue = Blueprint("mainBlue", __name__)

@mainBlue.route("/")
def dashboard():
    return render_template("dashboard.html")