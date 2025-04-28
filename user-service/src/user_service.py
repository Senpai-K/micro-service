from flask import Flask, jsonify, request

app = Flask(__name__)
users = []

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if not username or not password:
		return jsonify({'error': 'Invalid username or password'}), 400
	user = {'username': username, 'password': password}
	users.append(user)
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
# Реализация аутентификации пользователя
def login_user():
	return jsonify({'token': 'user_token'})

if __name__ == '__main__':
	app.run(debug=True, port=5002, host='0.0.0.0')

