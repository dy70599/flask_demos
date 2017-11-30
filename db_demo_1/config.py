# -*- coding: utf-8 -*-#

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo_1'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT,
                                                 DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACE_MODIFICATIONS = True
