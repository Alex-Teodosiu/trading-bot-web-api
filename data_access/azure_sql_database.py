import pyodbc
from dotenv import load_dotenv


class AzureSQLDatabase:
    def __init__(self):
        self._server = 'tradingplatformserver.database.windows.net'
        self._database = 'tradingplatformdb'
        self._username = 'CloudSA25ca4491'
        self._password = 'Azure123!'
        self._driver = '{ODBC Driver 17 for SQL Server}'
        

    def get_db_connection(self):
        load_dotenv()
        connection = pyodbc.connect(self.get_connection_string())
        return connection

    def get_connection_string(self):
        return 'DRIVER=' + self._driver + ';SERVER=' + self._server + ';PORT=1433;DATABASE=' + self._database + ';UID=' + self._username + ';PWD=' + self._password