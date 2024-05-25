
from flask_restx import Namespace, Resource
from flask import request  
from services.asset_service import AssetService


assets = Namespace('assets')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._asset_service = AssetService()
    

@assets.route('/getcryptoassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_crypto_assets(), 200
    

@assets.route('/getNYSEstockassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_NYSE_stock_assets(), 200
    

@assets.route('/getOTCstockassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_OTC_stock_assets(), 200
    

@assets.route('/getARCAstockassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_ARCA_stock_assets(), 200
    

@assets.route('/getAMEXstockassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_AMEX_stock_assets(), 200
    
@assets.route('/getBATSstockassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_BATS_stock_assets(), 200
    

@assets.route('/getNASDAQstockassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_NASDAQ_stock_assets(), 200
