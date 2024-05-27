from data_access.azure_sql_database import AzureSQLDatabase
from models.algorithm_model import Algorithm

class AlgorithmRepository:
    def __init__(self):
        self._db = AzureSQLDatabase()

    def get_algorithms(self):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [algorithm]")
        users = cursor.fetchall()
        conn.close()
        return users
    

    def get_algorithms_by_user_id(self, user_id):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [algorithm] WHERE USER_ID = ?", (user_id,))
        db_algos = cursor.fetchall()

        if not db_algos:
            return None

        algorithms = [Algorithm(db_algo[1], db_algo[2], db_algo[3], db_algo[4]).to_dict() for db_algo in db_algos]
        conn.close()
        return algorithms
    
    
    def save_algorithm_run(self, algorithm):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO [algorithm] (ALGORITHM_NAME, SYMBOL, USER_ID, TIME_STAMP) VALUES (?, ?, ?, ?)", (algorithm.algorithm_name, algorithm.symbol, algorithm.user_id, algorithm.time_stamp))
        conn.commit()
        conn.close()
        return algorithm.to_dict()
    
    
    def stop_algorithm(self, user_id, symbol, algorithm_name):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM [algorithm] WHERE USER_ID = ? AND SYMBOL = ? AND ALGORITHM_NAME = ?", (user_id, symbol, algorithm_name))
        conn.commit()
        conn.close()
        return {'message': f'{algorithm_name} algorithm has stopped running on {symbol}.'}
    

    def is_algorithm_running(self, user_id, symbol, algorithm_name):
        conn = self._db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [algorithm] WHERE USER_ID = ? AND SYMBOL = ? AND ALGORITHM_NAME = ?", (user_id, symbol, algorithm_name))
        db_algo = cursor.fetchone()
        conn.close()
        return db_algo is not None