from functions.open_order_func import getOpenOrder

from flask_restful import Resource, request
from flask import jsonify
import os
import json

class OpenOrder(Resource):
    def get(self):
        jsn = {}

        res = json.dumps(getOpenOrder())
        res = json.loads(res)
        res = res[0]

        jsn = {"status":res.get('status'), "message":res.get('message'),"body":res.get('body')}
 
        return jsn