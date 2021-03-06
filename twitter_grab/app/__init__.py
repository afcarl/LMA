# db setup goes here
from flask import Flask
from flask_script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from .commands import REPL
import os

username,password = "eric","1234"
app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://"+username+":"+password+"@localhost/congress"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("shell",REPL())

from app import models
