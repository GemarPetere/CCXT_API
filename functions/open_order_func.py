from decouple import config
import ccxt

def getOpenOrder():
    data = []

    try:
        exchange = ccxt.binance({
            'apiKey': config('APIKEY'),
            'secret': config('SECRETKEY')
        })

        # fetch the opoen order for BTC/USDT on Binance
        trading_pair = 'BTC/USDT'
        order = exchange.fetch_open_orders(trading_pair)
       
        data.append({"status": 200,
                        "message":"Open Orders", 
                        "body": order
                    })
        return data

    except Exception as error:
        data.append({"status": 500,"message": "Internal ccxt error", "body": {error}})

        return data

    