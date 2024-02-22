from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/utils', methods=['GET'])
def hello_utils():
    return 'Hello utils'

@app.route('/test', methods=['GET'])
def test():
    return "Hello"

if __name__ == '__main__':
    app.run(port=8000)

