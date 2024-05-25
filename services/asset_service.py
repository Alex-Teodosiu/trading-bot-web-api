
import requests
from models.asset_model import Asset, AssetExchange, AssetClass
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from flask import current_app

class AssetService:
    def __init__(self):
        self._api_key = current_app.config['ALPACA_API_KEY']
        self._secret_key = current_app.config['ALPACA_API_SECRET']
        self._trading_client = TradingClient(self._api_key, self._secret_key, paper=True)


    def get_crypto_assets(self):
        search_params = GetAssetsRequest(asset_class=AssetClass.CRYPTO)
        assets_data = self._trading_client.get_all_assets(search_params)
        assets = []
        for asset_data in assets_data:
            asset = self.create_asset_from_data(asset_data)
            assets.append(asset)
        assets_dict = [asset.to_dict() for asset in assets]
        return assets_dict
    

    def get_NYSE_stock_assets(self):
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        assets_data = self._trading_client.get_all_assets(search_params)
        # Filter assets_data to only include assets from the NYSE
        assets_data = [asset for asset in assets_data if 'NYSE' in asset.exchange]
        assets = []
        for asset_data in assets_data[1:100]:
            asset = self.create_asset_from_data(asset_data)
            assets.append(asset)
        assets_dict = [asset.to_dict() for asset in assets]
        return assets_dict


    def get_OTC_stock_assets(self):
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        assets_data = self._trading_client.get_all_assets(search_params)
        # Filter assets_data to only include assets from the NYSE
        assets_data = [asset for asset in assets_data if 'NYSE' in asset.exchange]
        assets = []
        for asset_data in assets_data[1:100]:
            asset = self.create_asset_from_data(asset_data)
            assets.append(asset)
        assets_dict = [asset.to_dict() for asset in assets]
        return assets_dict
    

    def get_ARCA_stock_assets(self):
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        assets_data = self._trading_client.get_all_assets(search_params)
        # Filter assets_data to only include assets from the NYSE
        assets_data = [asset for asset in assets_data if 'NYSE' in asset.exchange]
        assets = []
        for asset_data in assets_data[1:100]:
            asset = self.create_asset_from_data(asset_data)
            assets.append(asset)
        assets_dict = [asset.to_dict() for asset in assets]
        return assets_dict


    def get_AMEX_stock_assets(self):
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        assets_data = self._trading_client.get_all_assets(search_params)
        # Filter assets_data to only include assets from the NYSE
        assets_data = [asset for asset in assets_data if 'NYSE' in asset.exchange]
        assets = []
        for asset_data in assets_data[1:100]:
            asset = self.create_asset_from_data(asset_data)
            assets.append(asset)
        assets_dict = [asset.to_dict() for asset in assets]
        return assets_dict
    
    def get_BATS_stock_assets(self):
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        assets_data = self._trading_client.get_all_assets(search_params)
        # Filter assets_data to only include assets from the NYSE
        assets_data = [asset for asset in assets_data if 'NYSE' in asset.exchange]
        assets = []
        for asset_data in assets_data[1:10]:
            asset = self.create_asset_from_data(asset_data)
            assets.append(asset)
        assets_dict = [asset.to_dict() for asset in assets]
        return assets_dict


    def get_NASDAQ_stock_assets(self):
        search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
        assets_data = self._trading_client.get_all_assets(search_params)
        # Filter assets_data to only include assets from the NYSE
        assets_data = [asset for asset in assets_data if 'NYSE' in asset.exchange]
        assets = []
        for asset_data in assets_data[1:100]:
            asset = self.create_asset_from_data(asset_data)
            assets.append(asset)
        assets_dict = [asset.to_dict() for asset in assets]
        return assets_dict


    def create_asset_from_data(self, asset_data):
        return Asset(
            asset_class=asset_data.asset_class,
            attributes=asset_data.attributes,
            easy_to_borrow=asset_data.easy_to_borrow,
            exchange=asset_data.exchange,
            fractionable=asset_data.fractionable,
            id=asset_data.id,
            maintenance_margin_requirement=asset_data.maintenance_margin_requirement,
            marginable=asset_data.marginable,
            min_order_size=asset_data.min_order_size,
            min_trade_increment=asset_data.min_trade_increment,
            name=asset_data.name,
            price_increment=asset_data.price_increment,
            shortable=asset_data.shortable,
            status=asset_data.status,
            symbol=asset_data.symbol,
            tradable=asset_data.tradable
        )
    
