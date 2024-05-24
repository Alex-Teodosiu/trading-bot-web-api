# from flask import request
# from flask_restx import Namespace, Resource
# from services.market_status_service import MarketStatus
# from flask_restx import Namespace, Resource


# marketstatus = Namespace('market-status')
# api = Namespace('api') 
# market_status_service = MarketStatus()


# @marketstatus.route('/get-market-status')
# @api.doc(params={'user_id':'User ID is required'})
# class GetAllOpenTrades(Resource):
#     def get(self):
#         user_id = request.args.get('user_id')
#         return market_status_service.get_market_status(user_id), 200