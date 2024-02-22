from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/utils')
def hello_utils():
    return 'Hello utils'

if __name__ == '__main__':
    app.run()

