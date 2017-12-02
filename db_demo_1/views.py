# -*- coding: utf-8 -*-#

from flask import Flask, render_template, request
from exts import db
from models import User
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        pass


if __name__ == "__main__":
    app.run(debug=True)