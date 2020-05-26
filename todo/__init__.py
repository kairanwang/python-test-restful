from flask import Blueprint

todo_api = Blueprint("todo", __name__)

from todo import views

