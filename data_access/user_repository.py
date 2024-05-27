from data_access.azure_sql_database import AzureSQLDatabase
from models.user_model import User

class UserRepository:
    def __init__(self):
        self._db = AzureSQLDatabase()

    def get_users(self):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [user]")
        users = cursor.fetchall()
        conn.close()
        return users
    

    def get_user_by_email(self, email):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [user] WHERE EMAIL = ?", email)
        db_user = cursor.fetchone()

        if db_user is None:
            return None
        
        user = User(db_user[1], db_user[2], db_user[0])
        print("user object")
        print(user)

        conn.close()
        return user
    

    def get_user_by_id(self, id):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [user] WHERE ID = ?", id)
        db_user = cursor.fetchone()

        if db_user is None:
            return None
        
        user = User(db_user[1], db_user[2], db_user[0])

        conn.close()
        return user
    

    def save_user(self, user):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO [user] (EMAIL, PASSWORD) VALUES (?, ?)", 
                       (user.get_email(), user.get_password()))

        conn.commit()
        conn.close()


    def update_user(self, id, password):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE [user] SET PASSWORD = ? WHERE id = ?", 
                       (password, id))

        conn.commit()
        conn.close()


    def delete_user(self, user_id):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM [user] WHERE ID = ?", user_id)

        conn.commit()
        conn.close()
        return True