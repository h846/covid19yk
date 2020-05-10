# -*- coding: utf-8 -*-
from flask import *
from flask_cors import CORS

import json
import re

api = Flask(__name__)
api.config["JSON_AS_ASCII"] = False
CORS(api)
#load json file
def loadJSON ():
    with open('data.json','r') as f:
        return json.load(f)

@api.route("/api/<name>", methods=['GET'])
def get_json(name):
    raw_data = loadJSON()
    if name not in raw_data:
        return "This is URL does not match any JSON data."
    
    proc_data = raw_data[name]
    keys = list(proc_data.keys())
    vals = list(proc_data.values())

    #データセットのvalsの中身を"人"やカンマを取り除き、数字だけ抽出する
    vals = [int(re.sub("\\D", "", n)) for n in vals]

    return jsonify({'keys': keys, 'vals': vals})

if __name__ == "__main__":
    api.run()