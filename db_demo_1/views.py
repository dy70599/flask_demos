# -*- coding: utf-8 -*-#

from flask import Flask, render_template
from exts import db
from models import User
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)