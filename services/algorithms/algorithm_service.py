from data_access.algorithm_repository import AlgorithmRepository

class AlgorithmService:
    def __init__(self):
        self.algorithm_repository = AlgorithmRepository()

    
    def get_all_algorithms(self, user_id):
        try:
            return self.algorithm_repository.get_algorithms_by_user_id(user_id)
        except:
            return {'Algorithms not found' }, 500
    
    def create_algorithm(self, algorithm):
        try:
            return self.algorithm_repository.save_algorithm_run(algorithm)
        except:
            return {'Algorithm not created' }, 500
        
    def stop_algorithm(self, user_id, symbol, algorithm_name):
        try:
            return self.algorithm_repository.stop_algorithm(user_id, symbol, algorithm_name)
        except:
            return {'Algorithm not stopped' }, 500

    