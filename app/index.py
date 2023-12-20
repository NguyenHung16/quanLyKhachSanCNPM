from flask import render_template, request, redirect
from app import app
import cloudinary.uploader
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    from app.admin import *
    app.run(debug=True)
