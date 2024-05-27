from data_access.algorithm_repository import AlgorithmRepository
from services.algorithms.momentum_algorithm_service import MomentumAlgorithmService
from services.algorithms.bollinger_algorithm_service import BollingerAlgorithmService
import threading

class AlgorithmService:
    def __init__(self):
        self.algorithm_repository = AlgorithmRepository()
        self._momentum_algorithm_service = MomentumAlgorithmService()
        self._bollinger_bands_service = BollingerAlgorithmService()

    
    def get_all_algorithms(self, user_id):
        try:
            return self.algorithm_repository.get_algorithms_by_user_id(user_id)
        except:
            return {'Algorithms not found' }, 500
    
    def create_algorithm(self, algorithm):
        try:
            algo_created = self.algorithm_repository.save_algorithm_run(algorithm)
            if algorithm.algorithm_name == 'Momentum':
                threading.Thread(target=self._momentum_algorithm_service.run_algorithm, args=(algorithm.user_id, algorithm.symbol)).start()
            elif algorithm.algorithm_name == 'Bollinger':
                threading.Thread(target=self._bollinger_bands_service.run_algorithm, args=(algorithm.user_id, algorithm.symbol)).start()
        except Exception as e:
            print(e)
            return e, 500
        
        return algo_created
    
    
    def stop_algorithm(self, user_id, symbol, algorithm_name):
        try:
            return self.algorithm_repository.stop_algorithm(user_id, symbol, algorithm_name)
        except:
            return {'Algorithm not stopped' }, 500

    