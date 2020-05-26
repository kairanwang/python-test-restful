from model import api
from todo import todo_api
from user import user_api

api.register_blueprint(user_api, url_prefix='/user')
api.register_blueprint(todo_api, url_prefix='/todo')

if __name__ == '__main__':
    api.run(debug=True)
