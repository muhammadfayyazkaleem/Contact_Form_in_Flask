from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)














# from flask import Flask , render_template, request
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

# DB_NAME = "contact_info.db"
# app.config['SECRET_KEY'] = "FayyazKaleem724"
# app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'   
# db.init_app(app)

# @app.route("/" , methods=['GET', 'POST'])
# def contact_form():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')

#         return message
#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)