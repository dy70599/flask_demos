# -*- coding: utf-8 -*-#

from flask_script import Manager
from views import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import User

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
