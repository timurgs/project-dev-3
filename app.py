from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from celery import Celery

import config
import os


app_name = 'app'
app = Flask(app_name)
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.POSTGRES_URI, SQLALCHEMY_TRACK_MODIFICATIONS=False)
app.secret_key = os.urandom(24)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

celery = Celery(app_name, broker='redis://redis:6379/0', backend='redis://redis:6379/1')


class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)


celery.Task = ContextTask
