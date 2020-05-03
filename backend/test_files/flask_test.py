from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()