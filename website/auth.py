from flask import Blueprint, render_template, request, flash , redirect

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def admin_login():
    if request.method == "POST":
        if request.form.get("username")== "user" and request.form.get("password")=='123456':
            flash("Login successful!" ,category='success')
            return redirect('/admin_page')
        else:
            flash("Incorrect username or password. Please try again." , category='error' )
            return redirect('/login')
    return render_template('admin_login.html')