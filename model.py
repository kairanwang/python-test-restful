from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config['SECRET_KEY'] = 'thisissecret'
api.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Www.163.com@39.97.107.142:3306/testrestapi?charset=utf8'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(api)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)