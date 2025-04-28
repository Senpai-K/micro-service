from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "description": "Task 1", "user_id": None, "completed": False},
    {"id": 2, "description": "Task 2", "user_id": None, "completed": True}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_tasks():
    data = request.get_json()
    description = data.get('description')
    if not description:
        return jsonify({'error': 'Task description is required'}), 400
    user_id = data.get('user_id')
    task = {'id': len(tasks) + 1, 'description': description, 'user_id': user_id, 'completed': False}
    tasks.append(task)
    return jsonify({'message': 'Task created successfully', 'id': task['id']}), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    description = data.get('description')
    if not description:
        return jsonify({'error': 'Task description is required'}), 400
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['completed'] = data.get('completed', task['completed'])
            return jsonify({'message': 'Task updated'})
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            return jsonify({'message': 'Task deleted'})
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
