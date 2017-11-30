# -*- coding: utf-8 -*-#

from flask_script import Manager
from views import app
from flask_migrate import Migrate
from exts import db

migrate = Migrate(app, db)
db_manager = Manager()


@db_manager.command()
def db_init():
    pass
