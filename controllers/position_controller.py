from flask import request, jsonify
from flask_restx import Namespace, Resource
from services.position_service import PositionService

positions = Namespace('positions')
api = Namespace('api') 
position_service = PositionService()


@positions.route('/get-all-open-positions')
@api.doc(params={'user_id':'User ID is required'})
class GetAllOpenTrades(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        return position_service.get_all_open_positions(user_id), 200
    
@positions.route('/close-all-open-positions')
@api.doc(params={'user_id':'User ID is required'})
class CloseAllOpenPositions(Resource):
    def delete(self):
        user_id = request.args.get('user_id')
        return position_service.close_all_open_positions(user_id), 200
    
@positions.route('/close-position-by-symbol')
@api.doc(params={'user_id':'User ID is required', 'symbol':'Symbol is required'})
class ClosePositionBySymbol(Resource):
    def delete(self):
        user_id = request.args.get('user_id')
        symbol = request.args.get('symbol')
        return position_service.close_position_by_symbol(user_id, symbol), 200
