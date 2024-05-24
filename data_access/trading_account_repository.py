from data_access.azure_sql_database import AzureSQLDatabase

class TradingAccountRepository:
    def __init__(self):
        self._db = AzureSQLDatabase()

    def get_accounts(self):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trading_account")
        accounts = cursor.fetchall()
        conn.close()
        return accounts
    

    #remove cursor from the function signature
    def account_exists(self, cursor, id: str) -> bool:
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM trading_account WHERE id = ?", (id,))
        result = cursor.fetchone() is not None
        conn.close()
        return result


    def save_account(self, user_id, account):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        try:
            if self.account_exists(cursor, account.id):
                # Update the account if the account already exists
                cursor.execute("""
                    UPDATE trading_account
                    SET api_key = ?, api_secret = ?, account_number = ?, status = ?, crypto_status = ?, currency = ?, buying_power = ?, 
                        regt_buying_power = ?, daytrading_buying_power = ?, non_marginable_buying_power = ?, cash = ?, 
                        accrued_fees = ?, pending_transfer_out = ?, pending_transfer_in = ?, portfolio_value = ?, 
                        pattern_day_trader = ?, trading_blocked = ?, transfers_blocked = ?, account_blocked = ?, 
                        created_at = ?, trade_suspended_by_user = ?, multiplier = ?, shorting_enabled = ?, 
                        equity = ?, last_equity = ?, long_market_value = ?, short_market_value = ?, initial_margin = ?, 
                        maintenance_margin = ?, last_maintenance_margin = ?, sma = ?, daytrade_count = ?, 
                        options_buying_power = ?, options_approved_level = ?, options_trading_level = ?, user_id = ?
                    WHERE id = ?
                """, (
                    account.api_key, account.api_secret, account.account_number, account.status, account.crypto_status, account.currency, account.buying_power, 
                    account.regt_buying_power, account.daytrading_buying_power, account.non_marginable_buying_power, account.cash, 
                    account.accrued_fees, account.pending_transfer_out, account.pending_transfer_in, account.portfolio_value, 
                    account.pattern_day_trader, account.trading_blocked, account.transfers_blocked, account.account_blocked, 
                    account.created_at, account.trade_suspended_by_user, account.multiplier, account.shorting_enabled, 
                    account.equity, account.last_equity, account.long_market_value, account.short_market_value, account.initial_margin, 
                    account.maintenance_margin, account.last_maintenance_margin, account.sma, account.daytrade_count, 
                    account.options_buying_power, account.options_approved_level, account.options_trading_level, user_id, account.id
                ))
            else:
                # Insert a new row if the account doesn't exist
                cursor.execute("""
                    INSERT INTO trading_account (
                        id, api_key, api_secret, account_number, status, crypto_status, currency, buying_power, regt_buying_power, 
                        daytrading_buying_power, non_marginable_buying_power, cash, accrued_fees, pending_transfer_out, 
                        pending_transfer_in, portfolio_value, pattern_day_trader, trading_blocked, transfers_blocked, 
                        account_blocked, created_at, trade_suspended_by_user, multiplier, shorting_enabled, equity, 
                        last_equity, long_market_value, short_market_value, initial_margin, maintenance_margin, 
                        last_maintenance_margin, sma, daytrade_count, options_buying_power, options_approved_level, 
                        options_trading_level, user_id
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    account.id, account.api_key, account.api_secret, account.account_number, account.status, account.crypto_status, account.currency, account.buying_power, 
                    account.regt_buying_power, account.daytrading_buying_power, account.non_marginable_buying_power, account.cash, 
                    account.accrued_fees, account.pending_transfer_out, account.pending_transfer_in, account.portfolio_value, 
                    account.pattern_day_trader, account.trading_blocked, account.transfers_blocked, account.account_blocked, 
                    account.created_at, account.trade_suspended_by_user, account.multiplier, account.shorting_enabled, 
                    account.equity, account.last_equity, account.long_market_value, account.short_market_value, account.initial_margin, 
                    account.maintenance_margin, account.last_maintenance_margin, account.sma, account.daytrade_count, 
                    account.options_buying_power, account.options_approved_level, account.options_trading_level, user_id
                ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
        return account
    
    
    def get_account_by_credentials(self, user_id, api_key):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trading_account WHERE user_id = ? AND api_key = ?", (user_id, api_key))
        account = cursor.fetchone()
        conn.close()
        return account

    
    def delete_account(self, id):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM trading_account WHERE id = ?", id)
        conn.commit()
        conn.close()
        return id
        

    def get_account_by_user_id(self, user_id):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trading_account WHERE user_id = ?", user_id)
        account = cursor.fetchone()
        conn.close()
        return account