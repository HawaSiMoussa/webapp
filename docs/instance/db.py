import click
from flask_sqlalchemy import SQLAlchemy  # (1.)
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'  # (2.)

db = SQLAlchemy()  
db.init_app(app)
  