
from flask import request
from flask_restx import Namespace, Resource
from services.market_data_service import MarketDataService
from flask_restx import Namespace, Resource


market_data = Namespace('market-data')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._market_data_service = MarketDataService()


@market_data.route('/crypto_last_quote')
class MarketDataController(BaseResource):
    @api.doc(params={'symbol': 'Symbol is required'})
    def get(self):
        symbol = request.args.get('symbol')
        return self._market_data_service.get_crypto_last_quote_by_symbol(symbol)


@market_data.route('/stock_last_quote')
class MarketDataController(BaseResource):
    @api.doc(params={'symbol': 'Symbol is required'})
    def get(self):
        symbol = request.args.get('symbol')
        return self._market_data_service.get_stock_last_quote_by_symbol(symbol)


@market_data.route('/crypto_historical_market_data')
class MarketDataController(BaseResource):
    @api.doc(params={'symbol': 'Symbol is required', 'last_x_days': 'Number of days is required'})
    def get(self):
        symbol = request.args.get('symbol')
        last_x_days = int(request.args.get('last_x_days'))

        return self._market_data_service.get_crypto_market_data_by_symbol(symbol, last_x_days)
    

@market_data.route('/stock_historical_market_data')
class MarketDataController(BaseResource):
    @api.doc(params={'symbol': 'Symbol is required', 'last_x_days': 'Number of days is required'})
    def get(self):
        symbol = request.args.get('symbol')
        last_x_days = int(request.args.get('last_x_days'))

        return self._market_data_service.get_stock_market_data_by_symbol(symbol, last_x_days)
