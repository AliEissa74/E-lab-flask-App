from flask import Flask, redirect, url_for, render_template , request , flash

app = Flask(__name__)

#=================================home page========================
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
@app.route("/login")
def login():
    return render_template("login.html")

#===============================signup=========================
@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
