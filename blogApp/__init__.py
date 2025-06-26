from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('blogApp.config')
db = SQLAlchemy(app)
    
from blogApp import views, models