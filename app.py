from flask import Flask, redirect, url_for, render_template , request , flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

#===============================./DATABASE CREATION========================

#=================================home page========================
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

#===================================brain tumor===========================
@app.route("/brain-tumor")
def brain():
    return render_template("diagnoses/brain.html")

#===============================Chest x-ray=========================
@app.route("/chest-x-ray")
def chest():
    return render_template("diagnoses/xray.html")

#===============================Breast cancer=========================
@app.route("/breast-cancer")
def breast():
    return render_template("diagnoses/breast.html")

#===============================Skin cancer=========================
@app.route("/skin-cancer")
def skin():
    return render_template("diagnoses/skin.html")

#===============================Diabetes=========================
@app.route("/diabetes")
def diabete():
    return render_template("diagnoses/diabetes.html")


#===============================authentication===========================================

#===============================login=========================
@app.route("/login" , methods=['GET', 'POST'])
def login():
    return render_template("login.html")

#===============================signup=========================
@app.route("/signup" , methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
