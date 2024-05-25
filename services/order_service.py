from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from models.order_response_model import OrderResponse
from models.cancel_order_response_model import CancelOrderResponse
from data_access.trading_account_repository import TradingAccountRepository
import json


class OrderService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()
    

    def create_order(self, user_id, order):
        try:
            print(order)
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")
        # prepare order data
        market_order_data = MarketOrderRequest(
                    symbol=order.get_symbol(),
                    # notionial only valid for day market orders
                    # else use the qty field
                    # qty=order.get_qty(),
                    notional=order.get_notional(),
                    side=order.get_side(),
                    time_in_force=order.get_time_in_force()
                    )
        # Market order
        try:
            market_order = temp_trading_client.submit_order(order_data=market_order_data)
        except Exception:
            return("Failed to submit order.")
        order_response = self.create_order_response(market_order)
        return order_response.to_dict()
    

    def create_limit_order(self, user_id, order):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return("Failed to get trading account for user_id provided.")

        # prepare order data
        limit_order_data = LimitOrderRequest(
                    symbol=order.get_symbol(),
                    limit_price=order.get_limit_price(),
                    notional=order.get_notional(),
                    side=order.get_side(),
                    time_in_force=order.get_time_in_force()
                    )
        # Market order
        try:
            market_order = temp_trading_client.submit_order(order_data=limit_order_data)
        except Exception:
            return("Failed to submit order.")
        order_response = self.create_order_response(market_order)
        return order_response.to_dict()
    

    def get_all_orders(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return f"Failed to get trading account for user_id provided: {user_id}"
    
        # get all orders
        orders = temp_trading_client.get_orders()
        order_responses = []
        for order in orders:
            order_response = self.create_order_response(order)
            order_responses.append(order_response.to_dict())
        return order_responses


    def cancel_all_orders(self, user_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return f"Failed to get trading account for user_id provided: {user_id}"

        # attempt to cancel all open orders
        cancel_order_responses = temp_trading_client.cancel_orders()
        cancel_order_responses = []
        for response in cancel_order_responses:
            cancel_response = self.create_cancel_order_response(response)
            cancel_order_responses.append(cancel_response.to_dict())
        return cancel_order_responses
    

    def cancel_order_by_id(self, user_id, order_id):
        try:
            trading_account = self._trading_account_repository.get_account_by_user_id(user_id)
            api_key = trading_account.api_key
            secret_key = trading_account.api_secret
            temp_trading_client = TradingClient(api_key, secret_key, paper=True)
        except Exception:
            return f"Failed to get trading account for user_id provided: {user_id}"

        # attempt to cancel all open orders
        try:
            cancel_order_response = temp_trading_client.cancel_order_by_id(order_id)
        except Exception as e:
            return(json.loads(str(e))['message'])
        print(cancel_order_response)
        return cancel_order_response

    
    @staticmethod
    def is_json(myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True
        
    def create_cancel_order_response(self, order):
        return CancelOrderResponse(
            id=str(order.id),
            status=order.status
        )
    

    def create_order_response(self, order):
        return OrderResponse(
            id=str(order.id),
            client_order_id=order.client_order_id,
            created_at=order.created_at.isoformat(),
            updated_at=order.updated_at.isoformat(),
            submitted_at=order.submitted_at.isoformat(),
            filled_at=order.filled_at.isoformat() if order.filled_at else None,
            expired_at=order.expired_at.isoformat() if order.expired_at else None,
            canceled_at=order.canceled_at.isoformat() if order.canceled_at else None,
            failed_at=order.failed_at.isoformat() if order.failed_at else None,
            replaced_at=order.replaced_at.isoformat() if order.replaced_at else None,
            replaced_by=order.replaced_by,
            replaces=order.replaces,
            asset_id=str(order.asset_id),
            symbol=order.symbol,
            asset_class=order.asset_class,
            notional=order.notional,
            qty=order.qty,
            filled_qty=order.filled_qty,
            filled_avg_price=order.filled_avg_price,
            order_class=order.order_class,
            order_type=order.order_type,
            type=order.type,
            side=order.side,
            time_in_force=order.time_in_force,
            limit_price=order.limit_price,
            stop_price=order.stop_price,
            status=order.status,
            extended_hours=order.extended_hours,
            legs=order.legs,
            trail_percent=order.trail_percent,
            trail_price=order.trail_price,
            hwm=order.hwm,
            # subtag=order.subtag,
            # source=order.source
        )
     
