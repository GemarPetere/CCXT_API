import ccxt


def getCoinPrice(exchangeName: str):
    data = []
    ticker =[]

    try:
       
        my_exchange = exchangeName # example of crypto exchange 
        ticker1 = ['BTC','ETH'] # ticker list of the crypto pair
        ticker2 = 'USDT' # second ticker of the crypto pair

        for coin in ticker1:

            method_to_call = getattr(ccxt,my_exchange.lower()) # retrieving the # method from ccxt whose name matches the given exchange name
            exchange_obj = method_to_call() # defining an exchange object
            pair_price_data = exchange_obj.fetch_ticker(coin+'/'+ticker2)
            closing_price = pair_price_data['close']

            ticker.append({"coin_name":coin,"close_price":closing_price})

        if closing_price:
            data.append({"status": 200,
                         "message":"Coin Price", 
                         "body":{
                            "exchange":"Binance",
                            "coin_list":ticker 
                           }})
        return data

    except Exception as error:
        data.append({"status": 500,"message": "Internal ccxt error", "body": {error}})

        return data
    