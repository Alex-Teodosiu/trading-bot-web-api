
import threading
from flask import request
from flask_restx import Namespace, Resource
from services.algorithms.bollinger_algorithm_service import BollingerAlgorithmService
from services.algorithms.momentum_algorithm_service import MomentumAlgorithmService
from services.algorithms.algorithm_service import AlgorithmService
from models.algorithm_model import Algorithm


algorithm = Namespace('algorithms')
# api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._algorithm_service = AlgorithmService()
        self._three_consecutive_algorithm_service = MomentumAlgorithmService()
        self._bollinger_bands_service = BollingerAlgorithmService()
    
@algorithm.route('/get-all-algorithms-by-user')
class GetAllAlgorithms(BaseResource):
    def get(self):
        data = request.json
        user_id = data['user_id']
        return self._algorithm_service.get_all_algorithms(user_id)
    
@algorithm.route('/save-algorithm-run')
class CreateAlgorithm(BaseResource):
    @algorithm.expect(Algorithm)
    def post(self):
        data = request.json
        algorithm = Algorithm(
            algorithm_name=data['algorithm_name'],
            # qty=data['qty'],
            symbol=data['symbol'],
            user_id=data['user_id'],
            time_stamp=data['time_stamp']
        )
        print(algorithm.__str__())
        return self._algorithm_service.create_algorithm(algorithm)
    

@algorithm.route('/stop-algorithm')
class StopAlgorithm(BaseResource):
    def delete(self):
        data = request.json
        user_id = data['user_id']
        symbol = data['symbol']
        algorithm_name = data['algorithm_name']
        return self._algorithm_service.stop_algorithm(user_id, symbol, algorithm_name)
    
    
################################################################################### 
    
    
# @algorithm.route('/run-momentum-algorithm')
# class RunAlgorithm(BaseResource):
#     def post(self):
#         data = request.json
#         user_id = data['user_id']
#         symbol = data['symbol']
#         # Start the algorithm in a separate thread
#         threading.Thread(target=self._three_consecutive_algorithm_service.run_algorithm, args=(user_id, symbol)).start()
        
#         return {"message": "Algorithm started"}
    

# @algorithm.route('/run-bollinger-algorithm')
# class RunBollingerAlgorithm(BaseResource):
#     def post(self):
#         data = request.json
#         user_id = data['user_id']
#         symbol = data['symbol']
#         qty = data['qty']
#         interval = data.get('interval', 60)  # Default interval to 60 seconds if not provided
        
#         bollinger_algorithm_service = BollingerAlgorithmService()  # Instantiate the BollingerAlgorithmService
        
#         # Start the Bollinger Bands algorithm in a separate thread
#         threading.Thread(target=self._bollinger_bands_service.run_algorithm, args=(user_id, symbol, qty, interval)).start()
        
#         return {"message": "Bollinger Bands Algorithm started"}
