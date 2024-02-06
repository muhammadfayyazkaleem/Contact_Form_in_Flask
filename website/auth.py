from flask import Blueprint, render_template, request, flash , redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from website import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username = username).first()
        if str(user.password) == str(password):  # Check if user exists and password matches
            login_user(user, remember=True)
            flash("Login successful!", category='success')
            return redirect('/admin_page')
        else:
            flash("Incorrect username or password. Please try again.", category='error')
            return redirect('/login')

    return render_template('admin_login.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')