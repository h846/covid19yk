# -*- coding: utf-8 -*-
from flask import *
from flask_cors import CORS

import json
import re

api = Flask(__name__)
api.config["JSON_AS_ASCII"] = False #文字化け対策
CORS(api)

@api.route("/")
def hello():
    return "usage: http://84log.net/api/[the_data_you_want]"

@api.route("/api/<name>", methods=['GET'])
def get_json(name):

    #load json data
    with open('data.json','r') as f:
        raw_data = json.load(f)

    if name not in raw_data:
       return "This URL does not match any JSON data."

    if name in "updated":
        #time = str(raw_data["updated"])
        return jsonify(raw_data)

    if name in ('patient_situation', 'outbreak_per_ward', 'pcr_test_num'):
        proc_data = raw_data[name]
        keys = list(proc_data.keys())
        vals = list(proc_data.values())
        #データセットのvalsの中身を"人"やカンマを取り除き、数字だけ抽出する
        vals = [int(re.sub("\\D", "", n)) for n in vals]
        return jsonify({'keys': keys, 'vals': vals, })
    elif name == 'shop_list':
        return jsonify(raw_data[name])

if __name__ == "__main__":
    api.run("0.0.0.0", debug=True)