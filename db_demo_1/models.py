# -*- coding: utf-8 -*-#

from exts import db


class User(db.Model):
    __tablename = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(100), nullable=False)