from flask import Blueprint, request, render_template ,flash , redirect
from flask_login import login_required
from website import db
from .models import ContactInfo

views = Blueprint('views', __name__)

@views.route("/" , methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        new_query = ContactInfo(name=name, email = email ,message = message)
        db.session.add(new_query)
        db.session.commit()
        flash(' Your message has been successfully submitted.' , category='success')

        return redirect('/')
    return render_template("index.html")

@views.route('/admin_page')
@login_required
def admin_page():
    records = ContactInfo.query.all()
    return render_template("admin_page.html" , records = records)