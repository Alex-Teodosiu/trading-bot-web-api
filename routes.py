from flask_restx import Api, Resource
from controllers.user_controller import users
from controllers.trading_account_controller import tradingaccounts
from controllers.asset_controller import assets
from controllers.order_controller import orders
from controllers.position_controller import positions
from controllers.market_data_controller import market_data
from controllers.algorithm_controller import algorithm
from controllers.market_status_controller import marketstatus

class Home(Resource):
    def get(self):
        return {"message": "Welcome to the Trading Bot API"}

def initialize_routes(api: Api):
    api.add_namespace(users, path="/users")
    api.add_namespace(tradingaccounts, path="/trading-accounts")
    api.add_namespace(assets, path="/assets")
    api.add_namespace(orders, path="/orders")
    api.add_namespace(positions, path="/positions")
    api.add_namespace(market_data, path="/market-data")
    api.add_namespace(algorithm, path="/algorithm")
    api.add_namespace(marketstatus, path="/market-status")
