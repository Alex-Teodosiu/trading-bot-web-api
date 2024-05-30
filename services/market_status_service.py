import json
from models.clock_model import Clock
from data_access.trading_account_repository import TradingAccountRepository
from alpaca.trading.client import TradingClient


class MarketStatus:
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()

    def get_market_status(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")
        try:
            clock = temp_trading_client.get_clock()
        except Exception as e:
            return(json.loads(str(e))['message'])
        print("t")
        market_status = self.create_clock(clock)
        print("s")
        print(market_status.__str__())
        return market_status.to_dict()

    
    def create_clock(self, clock):
        return Clock(
            timestamp=str(clock.timestamp.isoformat()),
            is_open=clock.is_open,
            next_open=clock.next_open,
            next_close=clock.next_close
        )
