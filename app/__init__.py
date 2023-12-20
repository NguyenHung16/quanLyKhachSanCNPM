from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
app = Flask(__name__)

app.secret_key = '&%^&)7896987697*%^%&*^)*^*RTUYTIUY*^&%&*^%&(^(*'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/dataks?charset=utf8mb4" % quote('16122003')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

cloudinary.config(cloud_name='dwpktjxdc', api_key='955745518372633', api_secret='0nZAfRwWQyfN4C_eUpbUhW8s9pU')