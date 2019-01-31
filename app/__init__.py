import os
from flask import Flask
from flask_bcrypt import Bcrypt
sec = 'asdaskjdhaufsf897987'
# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

@app.route("/"+sec)
def hello():
    return "Hello World!"