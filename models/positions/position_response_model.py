class PositionResponse:
    def __init__(self, asset_id, symbol, exchange, asset_class, asset_marginable, avg_entry_price, qty, side, market_value, cost_basis, unrealized_pl, unrealized_plpc, unrealized_intraday_pl, unrealized_intraday_plpc, current_price, lastday_price, change_today, swap_rate, avg_entry_swap_rate, usd, qty_available):
        self.asset_id = asset_id
        self.symbol = symbol
        self.exchange = exchange
        self.asset_class = asset_class
        self.asset_marginable = asset_marginable
        self.avg_entry_price = avg_entry_price
        self.qty = qty
        self.side = side
        self.market_value = market_value
        self.cost_basis = cost_basis
        self.unrealized_pl = unrealized_pl
        self.unrealized_plpc = unrealized_plpc
        self.unrealized_intraday_pl = unrealized_intraday_pl
        self.unrealized_intraday_plpc = unrealized_intraday_plpc
        self.current_price = current_price
        self.lastday_price = lastday_price
        self.change_today = change_today
        self.swap_rate = swap_rate
        self.avg_entry_swap_rate = avg_entry_swap_rate
        self.usd = usd
        self.qty_available = qty_available

    def to_dict(self):
        return {
            'asset_id': self.asset_id,
            'symbol': self.symbol,
            'exchange': self.exchange,
            'asset_class': self.asset_class,
            'asset_marginable': self.asset_marginable,
            'avg_entry_price': self.avg_entry_price,
            'qty': self.qty,
            'side': self.side,
            'market_value': self.market_value,
            'cost_basis': self.cost_basis,
            'unrealized_pl': self.unrealized_pl,
            'unrealized_plpc': self.unrealized_plpc,
            'unrealized_intraday_pl': self.unrealized_intraday_pl,
            'unrealized_intraday_plpc': self.unrealized_intraday_plpc,
            'current_price': self.current_price,
            'lastday_price': self.lastday_price,
            'change_today': self.change_today,
            'swap_rate': self.swap_rate,
            'avg_entry_swap_rate': self.avg_entry_swap_rate,
            'usd': self.usd,
            'qty_available': self.qty_available
        }
