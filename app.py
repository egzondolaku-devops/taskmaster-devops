from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []
    
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks = load_tasks()

    if tasks:
        new_id = max(task.get('id', 0) for task in tasks) + 1
    else:
        new_id = 1
    new_task = {
        "id": new_id,
        "title": data.get('title'),
        "description": data.get('description'),
        "completed": False,
        "due_date": ""
    }
    tasks.append(new_task)
        

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file , indent=2)
        return jsonify(new_task), 201
    

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    task.update({
        "title": data.get('title', task['title']),
        "description": data.get('description', task['description']),
        "completed": data.get('completed', task['completed']),
        "due_date": data.get('due_date', task['due_date'])
    })
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file , indent=2)
        return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    tasks.remove(task)
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file , indent=2)
        return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)