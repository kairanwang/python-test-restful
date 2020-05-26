from flask import jsonify, request
from model import db, Todo
from todo import todo_api
from user.views import token_required


@todo_api.route('/', methods=['GET'])
@token_required
def get_all_todo(current_user):
    todos = Todo.query.filter_by(user_id=current_user.id).all()

    output = []

    for todo in todos:
        todo_data = {'id': todo.id, 'text': todo.text, 'complete': todo.complete}
        output.append(todo_data)

    return jsonify({'message': output})


@todo_api.route('/<todo_id>', methods=['GET'])
@token_required
def get_one_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})
    todo_data = {'id': todo.id, 'text': todo.text, 'complete': todo.complete}

    return jsonify({todo_data})

    return ''


@todo_api.route('/', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()

    new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)

    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'message': 'Todo created!'})


@todo_api.route('/<todo_id>', methods=['PUT'])
@token_required
def complete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})
    todo.complete = True
    db.session.commit()

    return jsonify({'message': 'Todo has completed!'})


@todo_api.route('/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})
    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message': 'Todo has deleted!'})

