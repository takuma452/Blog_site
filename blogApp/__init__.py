from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('blogApp.config')

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
    
import blogApp.views