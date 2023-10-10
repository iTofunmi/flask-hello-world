from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/data', methods=['GET'])
def api_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)