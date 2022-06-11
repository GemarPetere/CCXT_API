"""App Server main"""

# importing dependencies or modules
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS


# importing modules
from resources.coin_prices_res import CoinPrices
from resources.open_order_res import OpenOrder

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)



api.add_resource(CoinPrices, '/api/v1/coinPrices')
api.add_resource(OpenOrder,'/api/v1/openOrder')



# Run the main app
if __name__ == '__main__':
    from waitress import server
    serve(app,host="192.168.1.45",port=8080)