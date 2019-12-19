from flask import *
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)
api = Api(app)

todos = {
    'todo1': {'task1':'Give Test1'},
    'todo2': {'task2':'Give Test2'},
    'todo3': {'task3':'Read documentation of Flask Restful API'}
}

def abort_if_todo_doesnt_exit(todo_id):
    if todo_id not in todos:
        abort(404,message='Todo {} doesnot exist'.format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
    def get(self,todo_id):
        abort_if_todo_doesnt_exit(todo_id)
        return todos[todo_id]
    def delete(self, todo_id):
        abort_if_todo_doesnt_exit(todo_id)
        del todos[todo_id]
        return '',204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        todos[todo_id] = task
        return task, 201

class TodoList(Resource):
    def get(self):
        return todos

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(todos.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        todos[todo_id] = {'task': args['task']}
        return todos[todo_id], 201


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)


