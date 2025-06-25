import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SACRET_KEY=os.getenv('SECRET_KEY', 'fallback-secret-key')
SQLALCHEMY_DATABASE_URI = 'sqlite:///blogs.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
