from flask import Flask, jsonify, request
import json
app = Flask(__name__)

decoded_object = json.loads(request.data)

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

todos = [
    { "label": "Sample", "done": True }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    todos.apppend(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

json.loads(request.data)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)