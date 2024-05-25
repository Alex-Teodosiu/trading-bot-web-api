from data_access.trading_account_repository import TradingAccountRepository
from models.trading_account_model import TradingAccount
from alpaca.trading.client import TradingClient
from alpaca.common.exceptions import APIError
from flask import current_app

class TradingAccountService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()
        self._api_key = current_app.config['ALPACA_API_KEY']
        self._secret_key = current_app.config['ALPACA_API_SECRET']
        self._trading_client = TradingClient(self._api_key, self._secret_key, paper=True)
    

    def get_account_by_credentials(self, user_id, api_key, secret):
        try:
            temp_trading_client = TradingClient(api_key, secret, paper=True)
            try:
                account_data = temp_trading_client.get_account()
            except Exception as e:
                return(f"An error occurred while getting the account from the Alpaca server: {e}")
            
            account = self.create_trading_account_object(account_data, user_id, api_key, secret)
            try:
                self._trading_account_repository.save_account(user_id, account)
            except Exception as e:
                return(f"An error occurred while validating the account: {e}")
                
            account = self.create_trading_account_object(account_data, user_id, api_key, secret)
            return account.to_dict()
        except APIError as e:
            return str(e)
        

    def get_account_by_user_id(self, user_id):
        try:
            account = self._trading_account_repository.get_account_by_user_id(user_id)
            if account is not None:
                _, api_key, api_secret, *_ = account
                # print(f"API Key: {api_key}, API Secret: {api_secret}")
                return self.get_account_by_credentials(user_id, api_key, api_secret)
            else:
                return "Account not found"
        except:
            return "Account not found"
        
    
    def delete_account(self, user_id, api_key):
        try:
            account = self._trading_account_repository.get_account_by_credentials(user_id, api_key)
            if account is not None:
                self._trading_account_repository.delete_account(account.id)
                return "Account deleted successfully"
            else:
                return "Account not found"
        except Exception as e:
            return str(e)
        
    
    def create_trading_account_object(self, account_data, user_id, api_key, secret):
        account = TradingAccount(
            id=account_data.id,
            api_key=api_key,
            api_secret=secret,
            account_number=account_data.account_number,
            status=account_data.status,
            crypto_status=account_data.crypto_status,
            currency=account_data.currency,
            buying_power=account_data.buying_power,
            regt_buying_power=account_data.regt_buying_power,
            daytrading_buying_power=account_data.daytrading_buying_power,
            non_marginable_buying_power=account_data.non_marginable_buying_power,
            cash=account_data.cash,
            accrued_fees=account_data.accrued_fees,
            pending_transfer_out=account_data.pending_transfer_out,
            pending_transfer_in=account_data.pending_transfer_in,
            portfolio_value=account_data.portfolio_value,
            pattern_day_trader=account_data.pattern_day_trader,
            trading_blocked=account_data.trading_blocked,
            transfers_blocked=account_data.transfers_blocked,
            account_blocked=account_data.account_blocked,
            created_at=account_data.created_at,
            trade_suspended_by_user=account_data.trade_suspended_by_user,
            multiplier=account_data.multiplier,
            shorting_enabled=account_data.shorting_enabled,
            equity=account_data.equity,
            last_equity=account_data.last_equity,
            long_market_value=account_data.long_market_value,
            short_market_value=account_data.short_market_value,
            initial_margin=account_data.initial_margin,
            maintenance_margin=account_data.maintenance_margin,
            last_maintenance_margin=account_data.last_maintenance_margin,
            sma=account_data.sma,
            daytrade_count=account_data.daytrade_count,
            options_buying_power=account_data.options_buying_power,
            options_approved_level=account_data.options_approved_level,
            options_trading_level=account_data.options_trading_level,
            user_id=user_id
        )
        return account
