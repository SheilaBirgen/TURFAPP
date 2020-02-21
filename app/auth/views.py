from flask import render_template, request, redirect, url_for
from . import auth
from flask_login import login_user,logout_user, current_user
from ..models import User

@auth.route('/register', methods = ['GET','POST'])
def register():
    errors = []
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        if not username:
            errors.append("Must enter username")
            return render_template("register.html",errors=errors)
        password = form.get("password")
        if not password:
            errors.append("Must enter password")
            return render_template("register.html",errors=errors)
        password_confirm = form.get("password_confirm")
        if not password_confirm:
            errors.append("Must enter password confirm field")
            return render_template("register.html",errors=errors)
        if password_confirm !=  password:
            errors.append("Passwords do not match")
            return render_template("register.html",errors=errors)
        user = User.query.filter_by(username=username).first()
        if user:
            errors.append("User with that username already exists")
            return render_template("register.html",errors=errors)
        user = User(username=username)
        user.set_password(password)
        user.save()
        return redirect(url_for("auth.login"))
    return render_template("register.html",errors=errors)
