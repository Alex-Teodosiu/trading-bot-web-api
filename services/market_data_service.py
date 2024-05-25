from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest, CryptoBarsRequest, StockLatestQuoteRequest, StockBarsRequest
from models.quote_model import Quote
from datetime import datetime, timedelta
from alpaca.common.exceptions import APIError
from alpaca.data.timeframe import TimeFrame
from flask import current_app

class MarketDataService:
    def __init__(self):
        self._api_key = current_app.config['ALPACA_API_KEY']
        self._secret_key = current_app.config['ALPACA_API_SECRET']
        self._stock_client = StockHistoricalDataClient(self._api_key, self._secret_key)
        # No keys required for crypto data
        self._crypto_client = CryptoHistoricalDataClient()


    def get_stock_last_quote_by_symbol(self, symbol):
        request_params = StockLatestQuoteRequest(symbol_or_symbols=symbol)
        latest_quote = self._stock_client.get_stock_latest_quote(request_params)
        latest_quote[symbol].ask_price
        print(latest_quote)
        quote = Quote(
            ask_exchange=latest_quote[symbol].ask_exchange,
            ask_price=latest_quote[symbol].ask_price,
            ask_size=latest_quote[symbol].ask_size,
            bid_exchange=latest_quote[symbol].bid_exchange,
            bid_price=latest_quote[symbol].bid_price,
            bid_size=latest_quote[symbol].bid_size,
            conditions=latest_quote[symbol].conditions,
            symbol=latest_quote[symbol].symbol,
            tape=latest_quote[symbol].tape,
            timestamp=latest_quote[symbol].timestamp
        )
        print(quote.__str__())
        return quote.to_dict()
        
    
    def get_crypto_last_quote_by_symbol(self, symbol):
        request_params = CryptoLatestQuoteRequest(symbol_or_symbols=symbol)
        latest_quote = self._crypto_client.get_crypto_latest_quote(request_params)
        latest_quote = latest_quote[symbol].ask_price
        print(latest_quote)
        return latest_quote
    
    
    def get_crypto_market_data_by_symbol(self, symbol, last_x_days):
      try:
          end_date = datetime.now()
          start_date = end_date - timedelta(days=last_x_days)
          request_params = CryptoBarsRequest(
              symbol_or_symbols=[symbol],
              timeframe=TimeFrame.Day,
              start=start_date.strftime("%Y-%m-%d"),
              end=end_date.strftime("%Y-%m-%d")
          )
          btc_bars = self._crypto_client.get_crypto_bars(request_params)
          print(btc_bars)
          bars_df = btc_bars.df.to_json(orient='records')
          return bars_df
      except APIError as e:
          return str(e)
    

    def get_stock_market_data_by_symbol(self, symbol, last_x_days):
      try:
          end_date = datetime.now()
          start_date = end_date - timedelta(days=last_x_days)
          request_params = StockBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            start=start_date.strftime("%Y-%m-%d"),
            end=end_date.strftime("%Y-%m-%d")
          )
          stock_bars = self._stock_client.get_stock_bars(request_params)
          print(stock_bars)
          bars_df = stock_bars.df.to_json(orient='records')
          return bars_df
      except APIError as e:
          return str(e)