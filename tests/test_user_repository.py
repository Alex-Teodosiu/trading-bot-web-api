import unittest
from unittest.mock import patch, MagicMock
from data_access.azure_sql_database import AzureSQLDatabase
from data_access.user_repository import UserRepository
from models.user_model import User

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.user_repo = UserRepository()
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        print("--------User Repository Test Setup--------")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_save_user(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        user = User('test@example.com', 'password')

        print("Running test_save_user")
        self.user_repo.save_user(user)

        self.mock_cursor.execute.assert_called_with("INSERT INTO [user] (EMAIL, PASSWORD) VALUES (?, ?)",
                                                    (user.get_email(), user.get_password()))
        self.mock_conn.commit.assert_called()
        print("User saved successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_users(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchall.return_value = [(1, 'test@example.com', 'password')]

        print("Running test_get_users")
        users = self.user_repo.get_users()

        self.assertEqual(len(users), 1)
        self.mock_cursor.execute.assert_called_with("SELECT * FROM [user]")
        print("Users retrieved successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_user_by_email(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = (1, 'test@example.com', 'password')

        print("Running test_get_user_by_email")
        user = self.user_repo.get_user_by_email('test@example.com')

        self.assertIsNotNone(user)
        self.assertEqual(user.get_email(), 'test@example.com')
        self.mock_cursor.execute.assert_called_with("SELECT * FROM [user] WHERE EMAIL = ?", 'test@example.com')
        print("User retrieved by email successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_get_user_by_id(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = (1, 'test@example.com', 'password')

        print("Running test_get_user_by_id")
        user = self.user_repo.get_user_by_id(1)

        self.assertIsNotNone(user)
        self.assertEqual(user.get_id(), 1)
        self.mock_cursor.execute.assert_called_with("SELECT * FROM [user] WHERE ID = ?", 1)
        print("User retrieved by ID successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_update_user(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn

        print("Running test_update_user")
        self.user_repo.update_user(1, 'new_password')

        self.mock_cursor.execute.assert_called_with("UPDATE [user] SET PASSWORD = ? WHERE id = ?", 
                                                    ('new_password', 1))
        self.mock_conn.commit.assert_called()
        print("User updated successfully")

    @patch.object(AzureSQLDatabase, 'get_db_connection')
    def test_delete_user(self, mock_get_db_connection):
        mock_get_db_connection.return_value = self.mock_conn

        print("Running test_delete_user")
        result = self.user_repo.delete_user(1)

        self.assertTrue(result)
        self.mock_cursor.execute.assert_called_with("DELETE FROM [user] WHERE ID = ?", 1)
        self.mock_conn.commit.assert_called()
        print("User deleted successfully")

if __name__ == '__main__':
    unittest.main()
