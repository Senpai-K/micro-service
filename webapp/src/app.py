import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
TASK_SERVICE_URL = 'http://tasks-service:5001'
USER_SERVICE_URL = 'http://user-service:5002'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
	if request.method == 'GET':
		response = requests.get(f'{TASK_SERVICE_URL}/tasks')
		tasks = response.json()
		return render_template('tasks.html', tasks=tasks)
	elif request.method == 'POST':
		data = {'description': request.form['description']}
		response = requests.post(f'{TASK_SERVICE_URL}/tasks', json=data)
		return jsonify(response.json())

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	elif request.method == 'POST':
		data = {'username': request.form['username'], 'password': request.form['password']}
		response = requests.post(f'{USER_SERVICE_URL}/register', json=data)
		return jsonify(response.json())

if __name__ == "__main__":
	app.run(debug=True, port=5000, host='0.0.0.0')
