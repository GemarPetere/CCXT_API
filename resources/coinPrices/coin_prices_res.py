"""Do something Here!"""
from flask_restful import Resource, request
from flask import jsonify
import os
import json
from functions.coinPrices.coin_prices_func import getCoinPrice

class CoinPrices(Resource):
    def post(self):
        jsn = {}
        data = request.data
        data = json.loads(data)
        
        exchange = data.get('exchange_name')

        res = json.dumps(getCoinPrice(exchangeName=exchange))
        res = json.loads(res)
        res = res[0]

        jsn = {"status": res.get('status'), "message": res.get('message'),"body":res.get('body')}
 
        return jsn