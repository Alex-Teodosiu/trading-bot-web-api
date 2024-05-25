import time
import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta, timezone
from models.orders.order_model import Order
from ..order_service import OrderService
from ..trading_account_service import TradingAccountService

class ThreeConsecutiveAlgorithmService:
    def __init__(self):
        self.order_service = OrderService()
        self.trading_account_service = TradingAccountService()

    def trade_algorithm(self, client, user_id, symbol):
        try:
            # Define the time range to fetch the most recent 5 minutes of data
            end_time = datetime.now(tz=timezone.utc)
            start_time = end_time - timedelta(minutes=6)

            # Convert times to RFC3339 format
            end_time_str = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
            start_time_str = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')

            # Fetch recent market data from IEX feed
            bars = client.get_bars(symbol, tradeapi.TimeFrame.Minute, start=start_time_str, end=end_time_str, feed='iex').df
            print(end_time)
            print(bars)
            if len(bars) < 5:
                return {"error": "Not enough data to make a decision"}
            
            # Extract closing prices from the bars
            close_prices = bars['close'].tolist()
            print(f"Fetched close prices: {close_prices}")

            # Simple momentum strategy
            if close_prices[-1] > close_prices[-2]:
            # and close_prices[-2] > close_prices[-3]:
                print("!!!Try to sell")
                order = Order(
                    symbol=symbol,
                    notional=100,
                    side="sell",
                    time_in_force="day"
                )
                response = self.order_service.create_order(user_id, order)
            elif close_prices[-1] < close_prices[-2]: 
            # and close_prices[-2] < close_prices[-3]:
                print("try to Buy!!!")
                order = Order(
                    symbol=symbol,
                    notional=100,
                    side="buy",
                    time_in_force="day"
                )
                response = self.order_service.create_order(user_id, order)
            else:
                response = {"message": "No trade made"}

            print(f"Response: {response}")
            return response
        except Exception as e:
            return {"error": str(e)}

    def run_algorithm(self, user_id, symbol, interval=60):
        trading_account = self.trading_account_service.get_account_by_user_id(user_id)
        api_key = trading_account['api_key']
        secret_key = trading_account['api_secret']
        client = tradeapi.REST(api_key, secret_key, "https://paper-api.alpaca.markets", api_version='v2')
        while True:
            response = self.trade_algorithm(client, user_id, symbol)
            print(response)
            time.sleep(interval)
            
