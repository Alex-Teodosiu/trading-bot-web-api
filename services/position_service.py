from alpaca.trading.client import TradingClient
from models.positions.position_model import ClosedPosition
from models.positions.position_response_model import PositionResponse
from data_access.trading_account_repository import TradingAccountRepository
import json

class PositionService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()


    def get_all_open_positions(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")
        # get all open positions
        try:
            open_trades = temp_trading_client.get_all_positions()
        except Exception as e:
            return(json.loads(str(e))['message'])
        open_positions = []
        for position in open_trades:
            print(f"position: {position}")
            position_response = self.create_position_response(position)
            open_positions.append(position_response.to_dict())
        return open_positions


    def close_all_open_positions(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")
        try:
            # closes all position 
            closed_positions_response = temp_trading_client.close_all_positions()
            print(f"closed_positions_response: {closed_positions_response}")
            print(f"Type of closed_positions_response: {type(closed_positions_response)}")
        except Exception as e:
            return(json.loads(str(e))['message'])
        return "Closed all positions"
       

    def close_position_by_symbol(self, user_id, symbol):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception as e:
            return("Failed to get trading account for user_id provided.")
        try:
            closed_positions_response = temp_trading_client.close_position(symbol)
            print(f"closed_positions_response: {closed_positions_response}")
            print(f"Type of closed_positions_response: {type(closed_positions_response)}")
        except Exception as e:
            return json.loads(str(e))['message'] if self.is_json(str(e)) else str(e)
        
        closed_position = self.create_position_response(closed_positions_response)
                         
        return closed_position.to_dict()


    @staticmethod
    def is_json(myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True

    
    
    def create_position_response(self, position):
        if isinstance(position, tuple):
            position = position[0]
        return PositionResponse(
            asset_id=str(position.asset_id),
            symbol=position.symbol,
            exchange=position.exchange.value,
            asset_class=position.asset_class.value,
            asset_marginable=position.asset_marginable,
            avg_entry_price=position.avg_entry_price,
            qty=position.qty,
            side=position.side.value,
            market_value=position.market_value,
            cost_basis=position.cost_basis,
            unrealized_pl=position.unrealized_pl,
            unrealized_plpc=position.unrealized_plpc,
            unrealized_intraday_pl=position.unrealized_intraday_pl,
            unrealized_intraday_plpc=position.unrealized_intraday_plpc,
            current_price=position.current_price,
            lastday_price=position.lastday_price,
            change_today=position.change_today,
            swap_rate=position.swap_rate,
            avg_entry_swap_rate=position.avg_entry_swap_rate,
            usd=position.usd,
            qty_available=position.qty_available
        )
