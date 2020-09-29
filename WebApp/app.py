from flask import Flask
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)
App.config['SECRET_KEY'] = 'secret-key'
App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(App)

from routes import *


if __name__ == "__main__":
    App.run(debug=True)