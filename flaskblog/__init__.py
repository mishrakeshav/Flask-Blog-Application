from flask import Flask

#pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "fb40965f2a290c9e3cf71459eb611fe5"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flaskblog import routes