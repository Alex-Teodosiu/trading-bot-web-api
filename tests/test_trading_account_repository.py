import unittest
from unittest.mock import patch, MagicMock
from data_access.azure_sql_database import AzureSQLDatabase
from data_access.trading_account_repository import TradingAccountRepository

class TestTradingAccountRepository(unittest.TestCase):

    def setUp(self):
        self.account_repo = TradingAccountRepository()
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        print("--------Trading Account Repository Test Setup--------")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_save_account(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        account = MagicMock()
        account.id = '1'
        account.api_key = 'key'
        account.api_secret = 'secret'
        account.account_number = 'number'
        account.status = 'status'
        account.crypto_status = 'crypto_status'
        account.currency = 'currency'
        account.buying_power = 'buying_power'
        account.regt_buying_power = 'regt_buying_power'
        account.daytrading_buying_power = 'daytrading_buying_power'
        account.non_marginable_buying_power = 'non_marginable_buying_power'
        account.cash = 'cash'
        account.accrued_fees = 'accrued_fees'
        account.pending_transfer_out = 'pending_transfer_out'
        account.pending_transfer_in = 'pending_transfer_in'
        account.portfolio_value = 'portfolio_value'
        account.pattern_day_trader = 'pattern_day_trader'
        account.trading_blocked = 'trading_blocked'
        account.transfers_blocked = 'transfers_blocked'
        account.account_blocked = 'account_blocked'
        account.created_at = 'created_at'
        account.trade_suspended_by_user = 'trade_suspended_by_user'
        account.multiplier = 'multiplier'
        account.shorting_enabled = 'shorting_enabled'
        account.equity = 'equity'
        account.last_equity = 'last_equity'
        account.long_market_value = 'long_market_value'
        account.short_market_value = 'short_market_value'
        account.initial_margin = 'initial_margin'
        account.maintenance_margin = 'maintenance_margin'
        account.last_maintenance_margin = 'last_maintenance_margin'
        account.sma = 'sma'
        account.daytrade_count = 'daytrade_count'
        account.options_buying_power = 'options_buying_power'
        account.options_approved_level = 'options_approved_level'
        account.options_trading_level = 'options_trading_level'
        user_id = 'user_id'

        self.mock_cursor.fetchone.return_value = None

        print("Running test_save_account")
        saved_account = self.account_repo.save_account(user_id, account)

        self.assertEqual(saved_account, account)
        self.mock_conn.commit.assert_called()
        self.mock_cursor.execute.assert_called()
        print("Account saved successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_accounts(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchall.return_value = [(1, 'key', 'secret', 'number', 'status', 'crypto_status', 'currency', 
                                                   'buying_power', 'regt_buying_power', 'daytrading_buying_power', 
                                                   'non_marginable_buying_power', 'cash', 'accrued_fees', 
                                                   'pending_transfer_out', 'pending_transfer_in', 'portfolio_value', 
                                                   'pattern_day_trader', 'trading_blocked', 'transfers_blocked', 
                                                   'account_blocked', 'created_at', 'trade_suspended_by_user', 
                                                   'multiplier', 'shorting_enabled', 'equity', 'last_equity', 
                                                   'long_market_value', 'short_market_value', 'initial_margin', 
                                                   'maintenance_margin', 'last_maintenance_margin', 'sma', 
                                                   'daytrade_count', 'options_buying_power', 'options_approved_level', 
                                                   'options_trading_level', 'user_id')]

        print("Running test_get_accounts")
        accounts = self.account_repo.get_accounts()

        self.assertEqual(len(accounts), 1)
        self.mock_cursor.execute.assert_called_with("SELECT * FROM trading_account")
        print("Accounts retrieved successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_account_exists(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = True

        print("Running test_account_exists")
        result = self.account_repo.account_exists(self.mock_cursor, '1')

        self.assertTrue(result)
        self.mock_cursor.execute.assert_called_with("SELECT 1 FROM trading_account WHERE id = ?", ('1',))
        print("Account exists check passed")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_account_by_credentials(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = (1, 'key', 'secret', 'number', 'status', 'crypto_status', 'currency', 
                                                   'buying_power', 'regt_buying_power', 'daytrading_buying_power', 
                                                   'non_marginable_buying_power', 'cash', 'accrued_fees', 
                                                   'pending_transfer_out', 'pending_transfer_in', 'portfolio_value', 
                                                   'pattern_day_trader', 'trading_blocked', 'transfers_blocked', 
                                                   'account_blocked', 'created_at', 'trade_suspended_by_user', 
                                                   'multiplier', 'shorting_enabled', 'equity', 'last_equity', 
                                                   'long_market_value', 'short_market_value', 'initial_margin', 
                                                   'maintenance_margin', 'last_maintenance_margin', 'sma', 
                                                   'daytrade_count', 'options_buying_power', 'options_approved_level', 
                                                   'options_trading_level', 'user_id')

        print("Running test_get_account_by_credentials")
        account = self.account_repo.get_account_by_credentials('user_id', 'key')

        self.assertIsNotNone(account)
        self.mock_cursor.execute.assert_called_with("SELECT * FROM trading_account WHERE user_id = ? AND api_key = ?", ('user_id', 'key'))
        print("Account retrieved by credentials successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_account_by_user_id(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = (1, 'key', 'secret', 'number', 'status', 'crypto_status', 'currency', 
                                                   'buying_power', 'regt_buying_power', 'daytrading_buying_power', 
                                                   'non_marginable_buying_power', 'cash', 'accrued_fees', 
                                                   'pending_transfer_out', 'pending_transfer_in', 'portfolio_value', 
                                                   'pattern_day_trader', 'trading_blocked', 'transfers_blocked', 
                                                   'account_blocked', 'created_at', 'trade_suspended_by_user', 
                                                   'multiplier', 'shorting_enabled', 'equity', 'last_equity', 
                                                   'long_market_value', 'short_market_value', 'initial_margin', 
                                                   'maintenance_margin', 'last_maintenance_margin', 'sma', 
                                                   'daytrade_count', 'options_buying_power', 'options_approved_level', 
                                                   'options_trading_level', 'user_id')

        print("Running test_get_account_by_user_id")
        account = self.account_repo.get_account_by_user_id('user_id')

        self.assertIsNotNone(account)
        self.mock_cursor.execute.assert_called_with("SELECT * FROM trading_account WHERE user_id = ?", 'user_id')
        print("Account retrieved by user ID successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_delete_account(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn

        print("Running test_delete_account")
        result = self.account_repo.delete_account('1')

        self.assertEqual(result, '1')
        self.mock_cursor.execute.assert_called_with("DELETE FROM trading_account WHERE id = ?", '1')
        self.mock_conn.commit.assert_called()
        print("Account deleted successfully")

if __name__ == '__main__':
    unittest.main()
