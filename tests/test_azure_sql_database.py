import unittest
from data_access.azure_sql_database import AzureSQLDatabase
import pyodbc


class TestAzureSQLDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.db = AzureSQLDatabase()
        print("--------Azure SQL Database Test Setup--------")

    def test_get_connection_string(self):
        print("Running test_get_connection_string")
        connection_string = self.db.get_connection_string()
        expected_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=tradingplatformserver.database.windows.net;'
            'PORT=1433;DATABASE=tradingplatformdb;'
            'UID=CloudSA25ca4491;PWD=Azure123!'
        )
        self.assertEqual(connection_string, expected_string)
        print("Connection string verified successfully")

    def test_get_db_connection_success(self):
        print("Running test_get_db_connection_success")
        try:
            connection = self.db.get_db_connection()
            self.assertIsNotNone(connection)
            self.assertIsInstance(connection, pyodbc.Connection)
            print("Database connection established successfully")
        except pyodbc.Error as e:
            self.fail(f"Connection failed with error: {e}")

    def test_get_db_connection_failure(self):
        print("Running test_get_db_connection_failure")
        self.db._password = 'WrongPassword'
        with self.assertRaises(pyodbc.Error):
            self.db.get_db_connection()
        print("Database connection failure test passed")

if __name__ == '__main__':
    unittest.main()
