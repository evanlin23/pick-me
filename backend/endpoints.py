from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/utils", methods=["GET"])
def hello_utils():
    return "Hello utils"


@app.route("/test", methods=["GET"])
def test():
    return "Hello"
@app.route('/coords', methods=['POST'])
def processCoords():
    print("received coords")
    print(request.json()) # theoretically should be the coordinates


if __name__ == "__main__":
    app.run()
