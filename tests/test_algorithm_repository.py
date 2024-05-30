import unittest
from unittest.mock import patch, MagicMock
from data_access.azure_sql_database import AzureSQLDatabase
from data_access.algorithm_repository import AlgorithmRepository
from models.algorithm_model import Algorithm

class TestAlgorithmRepository(unittest.TestCase):

    def setUp(self):
        self.algo_repo = AlgorithmRepository()
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        print("--------Algorithm Repository Test Setup--------")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_save_algorithm_run(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        algorithm = Algorithm('Algo1', 'AAPL', 'user_id', '2023-01-01 00:00:00')

        print("Running test_save_algorithm_run")
        saved_algorithm = self.algo_repo.save_algorithm_run(algorithm)

        self.assertEqual(saved_algorithm['algorithm_name'], 'Algo1')
        self.mock_cursor.execute.assert_called_with(
            "INSERT INTO [algorithm] (ALGORITHM_NAME, SYMBOL, USER_ID, TIME_STAMP) VALUES (?, ?, ?, ?)",
            (algorithm._algorithm_name, algorithm._symbol, algorithm._user_id, algorithm._time_stamp)
        )
        self.mock_conn.commit.assert_called()
        print("Algorithm run saved successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_algorithms(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchall.return_value = [(1, 'Algo1', 'AAPL', 'user_id', '2023-01-01 00:00:00')]

        print("Running test_get_algorithms")
        algorithms = self.algo_repo.get_algorithms()

        self.assertEqual(len(algorithms), 1)
        self.mock_cursor.execute.assert_called_with("SELECT * FROM [algorithm]")
        print("Algorithms retrieved successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_algorithms_by_user_id(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchall.return_value = [(1, 'Algo1', 'AAPL', 'user_id', '2023-01-01 00:00:00')]

        print("Running test_get_algorithms_by_user_id")
        algorithms = self.algo_repo.get_algorithms_by_user_id('user_id')

        self.assertIsNotNone(algorithms)
        self.assertEqual(len(algorithms), 1)
        self.mock_cursor.execute.assert_called_with("SELECT * FROM [algorithm] WHERE USER_ID = ?", ('user_id',))
        print("Algorithms retrieved by user ID successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_stop_algorithm(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn

        print("Running test_stop_algorithm")
        result = self.algo_repo.stop_algorithm('user_id', 'AAPL', 'Algo1')

        self.assertEqual(result, {'message': 'Algo1 algorithm has stopped running on AAPL.'})
        self.mock_cursor.execute.assert_called_with(
            "DELETE FROM [algorithm] WHERE USER_ID = ? AND SYMBOL = ? AND ALGORITHM_NAME = ?",
            ('user_id', 'AAPL', 'Algo1')
        )
        self.mock_conn.commit.assert_called()
        print("Algorithm stopped successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_is_algorithm_running(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = True

        print("Running test_is_algorithm_running")
        result = self.algo_repo.is_algorithm_running('user_id', 'AAPL', 'Algo1')

        self.assertTrue(result)
        self.mock_cursor.execute.assert_called_with(
            "SELECT * FROM [algorithm] WHERE USER_ID = ? AND SYMBOL = ? AND ALGORITHM_NAME = ?",
            ('user_id', 'AAPL', 'Algo1')
        )
        print("Algorithm running check passed")

if __name__ == '__main__':
    unittest.main()
