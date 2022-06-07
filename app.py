"""App Server main"""


# importing dependencies or modules
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS


# importing modules
from resources.coinPrices.coin_prices_res import CoinPrices

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)



api.add_resource(CoinPrices, '/api/v1/coinPrices')



# Run the main app
if __name__ == '__main__':
    app.run(debug=True)