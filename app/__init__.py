from flask import Flask

app = Flask(__name__)

# Load config from config.py
app.config.from_object('config.Config')

from app import routes

