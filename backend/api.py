from flask import Flask, request, abort, make_response, current_app, jsonify
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    api.run(host='localhost', port=8080)