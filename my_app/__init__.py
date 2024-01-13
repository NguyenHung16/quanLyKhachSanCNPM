from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import  LoginManager
from urllib.parse import quote


app = Flask(__name__)
app.secret_key = '&%^&)7896987697*%^%&*^)*^*RTUYTIUY*^&%&*^%&(^(*'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/dbks1?charset=utf8mb4" % quote('16122003')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 6

db = SQLAlchemy(app=app)
admin = Admin(app=app, name="Quan Ly Khach San", template_mode="bootstrap5")
my_login = LoginManager(app=app)
nhanvien= admin.name