from flask import Flask
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route("/")
def hello():
    return "Hello World!"

@api.route("/test")
def test():
    return "TEST WORKS"

if __name__ == "__main__":
    api.run()