import time
import alpaca_trade_api as tradeapi
from ..order_service import OrderService
from .bollinger_bands import calculate_bollinger_bands
from data_access.algorithm_repository import AlgorithmRepository
import pandas as pd

class BollingerAlgorithmService:
    def __init__(self):
        self.order_service = OrderService()
        self.algorithm_repository = AlgorithmRepository()

    def get_historical_data(self, user_id, symbol):
        try:
            trading_account = self.order_service._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            client = tradeapi.REST(api_key, secret_key, "https://paper-api.alpaca.markets", api_version='v2')

            # Fetch historical data
            barset = client.get_barset(symbol, 'minute', limit=100)
            bars = barset[symbol]
            data = pd.DataFrame([bar._raw for bar in bars])
            return data
        except Exception as e:
            print(f"Error fetching historical data: {str(e)}")
            return None

    def trade_algorithm(self, user_id, symbol, qty):
        try:
            data = self.get_historical_data(user_id, symbol)
            if data is None or data.empty:
                return {"error": "Failed to retrieve historical data"}

            # Calculate Bollinger Bands
            data = calculate_bollinger_bands(data)

            # Simple trading strategy based on Bollinger Bands
            current_price = data['close'].iloc[-1]
            upper_band = data['upper_band'].iloc[-1]
            lower_band = data['lower_band'].iloc[-1]

            if current_price >= upper_band:
                response = self.order_service.create_order(user_id, symbol, qty, 'sell')
            elif current_price <= lower_band:
                response = self.order_service.create_order(user_id, symbol, qty, 'buy')
            else:
                response = {"message": "No trade made"}

            return response
        except Exception as e:
            return {"error": str(e)}

    def run_algorithm(self, user_id, symbol, interval=60):
        while self.algorithm_repository.is_algorithm_running(user_id, symbol, 'Bollinger'):
            response = self.trade_algorithm(user_id, symbol, 500)
            print(response)
            time.sleep(interval)
