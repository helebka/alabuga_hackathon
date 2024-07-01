from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from werkzeug.security import check_password_hash

from app.database.repository import UserRepository
from app.forms.login_form import LoginForm

authentication = Blueprint("authentication", __name__)
login_manager = LoginManager()
login_manager.init_app(authentication)


@authentication.route("/register", endpoint="registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email and password:
            UserRepository.create_user(email, password)
            flash("You have successfully created account!", "message")
            return redirect(url_for("authentication.login"))
        else:
            flash("Missing email or password field", "error")
            return redirect(url_for("authentication.registration"))
    return render_template("register.html", title="Registration")


@authentication.route("/login", endpoint="login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return "You are authenticated"
    form = LoginForm()
    if form.validate_on_submit():
        user = UserRepository.get_user_by_email(form.email.data)
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return "You are logged in"
            else:
                flash("Invalid password", "error")
        else:
            flash("Invalid email or account does not exist", "error")
            return redirect(url_for("authentication.login"))
    return render_template("login.html", title="Login", form=form)


@authentication.route("/logout", endpoint="logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "message")
    return redirect(url_for("authentication.login"))
