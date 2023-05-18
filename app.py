from flask import Flask, redirect, url_for, render_template , request , flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,LoginManager,login_required
from email_validator import validate_email, EmailNotValidError
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///DataBase.db"
app.config['SECRET_KEY']='E-LAB'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
bootstrap = Bootstrap(app)


Login_manager=LoginManager()
Login_manager.init_app(app)
Login_manager.login_view='login'


@Login_manager.user_loader
def Load_User(user_id):
    return User.query.get(int(user_id))



#DATABASE CREATION
class User(db.Model,UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(30),nullable=False) 


with app.app_context():
    db.create_all()



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
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate email and password
        if not email:
            flash('Please enter an email address.',category="danger")
            return redirect(url_for('login'))
        if not password:
            flash('Please enter a password.',category="danger")
            return redirect(url_for('login'))

        # Perform login action
        user = User.query.filter_by(email=email).first()
        if user is None:
            flash('Invalid email or password',category="danger")
            return redirect(url_for('login'))

        # Check if password is correct
        if not bcrypt.check_password_hash(user.password, password):
            flash('Invalid email or password',category="danger")
            return redirect(url_for('login'))

        # Login the user
        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')

#===============================signup=========================
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password1']
        confirm_password = request.form['password2']

        # check if username already exists in the database
        # existing_user = User.query.filter_by(username=username).first()
        if len(username) < 2:
            flash("name must be grater than 1 character." ,"danger")
            return redirect(url_for('signup'))

        # check if email is valid
        try:
            validate_email(email)
        except EmailNotValidError as e:
            flash(str(e))
            return redirect(url_for('signup'))

        # Check if email already exists in the database
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("This email address is already registered. Please use a different email." ,"danger")
            return redirect(url_for('signup'))


        # check if password and confirm password match
        if password != confirm_password:
            flash("Password and confirm password do not match." ,"danger")
            return redirect(url_for('signup'))

        # check if password less than 7 characters
        if len(password) < 8:
            flash("Password Must be at least 8 characters." ,"danger")
            return redirect(url_for('signup'))
        
        # create new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Your account has been created successfully!","success")
        return redirect(url_for('login'))

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)
