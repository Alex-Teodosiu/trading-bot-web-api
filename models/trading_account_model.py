
from datetime import datetime
from uuid import UUID

class TradingAccount:
    def __init__(self, id: UUID, api_key: str, api_secret: str, account_number: str, status: str, crypto_status: str, currency: str, buying_power: str, 
                 regt_buying_power: str, daytrading_buying_power: str, non_marginable_buying_power: str, cash: str, 
                 accrued_fees: str, pending_transfer_out: str, pending_transfer_in: str, portfolio_value: str, 
                 pattern_day_trader: bool, trading_blocked: bool, transfers_blocked: bool, account_blocked: bool, 
                 created_at: datetime, trade_suspended_by_user: bool, multiplier: str, shorting_enabled: bool, 
                 equity: str, last_equity: str, long_market_value: str, short_market_value: str, initial_margin: str, 
                 maintenance_margin: str, last_maintenance_margin: str, sma: str, daytrade_count: int, 
                 options_buying_power: str, options_approved_level: int, options_trading_level: int, user_id: UUID):
        self.id = id
        self.api_key = api_key
        self.api_secret = api_secret
        self.account_number = account_number
        self.status = status
        self.crypto_status = crypto_status
        self.currency = currency
        self.buying_power = buying_power
        self.regt_buying_power = regt_buying_power
        self.daytrading_buying_power = daytrading_buying_power
        self.non_marginable_buying_power = non_marginable_buying_power
        self.cash = cash
        self.accrued_fees = accrued_fees
        self.pending_transfer_out = pending_transfer_out
        self.pending_transfer_in = pending_transfer_in
        self.portfolio_value = portfolio_value
        self.pattern_day_trader = pattern_day_trader
        self.trading_blocked = trading_blocked
        self.transfers_blocked = transfers_blocked
        self.account_blocked = account_blocked
        self.created_at = created_at
        self.trade_suspended_by_user = trade_suspended_by_user
        self.multiplier = multiplier
        self.shorting_enabled = shorting_enabled
        self.equity = equity
        self.last_equity = last_equity
        self.long_market_value = long_market_value
        self.short_market_value = short_market_value
        self.initial_margin = initial_margin
        self.maintenance_margin = maintenance_margin
        self.last_maintenance_margin = last_maintenance_margin
        self.sma = sma
        self.daytrade_count = daytrade_count
        self.options_buying_power = options_buying_power
        self.options_approved_level = options_approved_level
        self.options_trading_level = options_trading_level
        self.user_id = user_id


    def to_dict(self):
        return {
            'id': str(self.id),
            'api_key': self.api_key,
            'api_secret': self.api_secret,
            'account_number': self.account_number,
            'status': self.status,
            'crypto_status': self.crypto_status,
            'currency': self.currency,
            'buying_power': self.buying_power,
            'regt_buying_power': self.regt_buying_power,
            'daytrading_buying_power': self.daytrading_buying_power,
            'non_marginable_buying_power': self.non_marginable_buying_power,
            'cash': self.cash,
            'accrued_fees': self.accrued_fees,
            'pending_transfer_out': self.pending_transfer_out,
            'pending_transfer_in': self.pending_transfer_in,
            'portfolio_value': self.portfolio_value,
            'pattern_day_trader': self.pattern_day_trader,
            'trading_blocked': self.trading_blocked,
            'transfers_blocked': self.transfers_blocked,
            'account_blocked': self.account_blocked,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
            'trade_suspended_by_user': self.trade_suspended_by_user,
            'multiplier': self.multiplier,
            'shorting_enabled': self.shorting_enabled,
            'equity': self.equity,
            'last_equity': self.last_equity,
            'long_market_value': self.long_market_value,
            'short_market_value': self.short_market_value,
            'initial_margin': self.initial_margin,
            'maintenance_margin': self.maintenance_margin,
            'last_maintenance_margin': self.last_maintenance_margin,
            'sma': self.sma,
            'daytrade_count': self.daytrade_count,
            'options_buying_power': self.options_buying_power,
            'options_approved_level': self.options_approved_level,
            'options_trading_level': self.options_trading_level,
            'user_id': self.user_id
        }


    def __str__(self):
        return (
            f"TradeAccount(\n"
            f"id={self.id},\n"
            f"api_key={self.api_key},\n"
            f"api_secret={self.api_secret},\n"
            f"account_number={self.account_number},\n"
            f"status={self.status},\n"
            f"crypto_status={self.crypto_status},\n"
            f"currency={self.currency},\n"
            f"buying_power={self.buying_power},\n"
            f"regt_buying_power={self.regt_buying_power},\n"
            f"daytrading_buying_power={self.daytrading_buying_power},\n"
            f"non_marginable_buying_power={self.non_marginable_buying_power},\n"
            f"cash={self.cash},\n"
            f"accrued_fees={self.accrued_fees},\n"
            f"pending_transfer_out={self.pending_transfer_out},\n"
            f"pending_transfer_in={self.pending_transfer_in},\n"
            f"portfolio_value={self.portfolio_value},\n"
            f"pattern_day_trader={self.pattern_day_trader},\n"
            f"trading_blocked={self.trading_blocked},\n"
            f"transfers_blocked={self.transfers_blocked},\n"
            f"account_blocked={self.account_blocked},\n"
            f"created_at={self.created_at},\n"
            f"trade_suspended_by_user={self.trade_suspended_by_user},\n"
            f"multiplier={self.multiplier},\n"
            f"shorting_enabled={self.shorting_enabled},\n"
            f"equity={self.equity},\n"
            f"last_equity={self.last_equity},\n"
            f"long_market_value={self.long_market_value},\n"
            f"short_market_value={self.short_market_value},\n"
            f"initial_margin={self.initial_margin},\n"
            f"maintenance_margin={self.maintenance_margin},\n"
            f"last_maintenance_margin={self.last_maintenance_margin},\n"
            f"sma={self.sma},\n"
            f"daytrade_count={self.daytrade_count},\n"
            f"options_buying_power={self.options_buying_power},\n"
            f"options_approved_level={self.options_approved_level},\n"
            f"options_trading_level={self.options_trading_level},\n"
            f"user_id={self.user_id}\n"
            f")"
        )
