
from enum import Enum
from uuid import UUID

class AssetClass(Enum):
    CRYPTO = 'crypto'
    US_EQUITY = 'us_equity'

class AssetExchange(Enum):
    CRYPTO = 'CRYPTO'
    US_EQUITY = 'US_EQUITY'
    ARCA = 'ARCA'
    BATS = 'BATS'
    OTC = 'OTC'
    NYSE = 'NYSE'
    NASDAQ = 'NASDAQ'
    AMEX = 'AMEX'

class AssetStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class Asset:
    def __init__(self, asset_class, attributes, easy_to_borrow, exchange, fractionable, id, maintenance_margin_requirement, marginable, min_order_size, min_trade_increment, name, price_increment, shortable, status, symbol, tradable):
        self.asset_class = AssetClass(asset_class) if isinstance(asset_class, str) else asset_class
        self.attributes = attributes
        self.easy_to_borrow = easy_to_borrow
        self.exchange = AssetExchange(exchange) if isinstance(exchange, str) else exchange
        self.fractionable = fractionable
        self.id = UUID(id) if isinstance(id, str) else id
        self.maintenance_margin_requirement = maintenance_margin_requirement
        self.marginable = marginable
        self.min_order_size = min_order_size
        self.min_trade_increment = min_trade_increment
        self.name = name
        self.price_increment = price_increment
        self.shortable = shortable
        self.status = AssetStatus(status) if isinstance(status, str) else status
        self.symbol = symbol
        self.tradable = tradable


    def to_dict(self):
        return {
            'asset_class': self.asset_class.value if isinstance(self.asset_class, Enum) else self.asset_class,
            'attributes': self.attributes,
            'easy_to_borrow': self.easy_to_borrow,
            'exchange': self.exchange.value if isinstance(self.exchange, Enum) else self.exchange,
            'fractionable': self.fractionable,
            'id': str(self.id) if isinstance(self.id, UUID) else self.id,
            'maintenance_margin_requirement': self.maintenance_margin_requirement,
            'marginable': self.marginable,
            'min_order_size': self.min_order_size,
            'min_trade_increment': self.min_trade_increment,
            'name': self.name,
            'price_increment': self.price_increment,
            'shortable': self.shortable,
            'status': self.status.value if isinstance(self.status, Enum) else self.status,
            'symbol': self.symbol,
            'tradable': self.tradable,
        }
    
    def __str__(self):
        return f'Asset(asset_class={self.asset_class}, attributes={self.attributes}, easy_to_borrow={self.easy_to_borrow}, exchange={self.exchange}, fractionable={self.fractionable}, id={self.id}, maintenance_margin_requirement={self.maintenance_margin_requirement}, marginable={self.marginable}, min_order_size={self.min_order_size}, min_trade_increment={self.min_trade_increment}, name={self.name}, price_increment={self.price_increment}, shortable={self.shortable}, status={self.status}, symbol={self.symbol}, tradable={self.tradable})'
