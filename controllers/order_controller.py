from services.order_service import OrderService
from models.orders.limit_order_model import LimitOrder
from models.orders.order_model import Order
from flask import request
from flask_restx import Namespace, Resource
from flask_restx import Namespace, Resource


orders = Namespace('orders')
api = Namespace('api') 
order_service = OrderService()

@orders.route('/create-order')
class TradeCreation(Resource):
    @orders.expect(Order)
    def post(self):
        data = request.json
        user_id = data['user_id']
        order = Order(
            symbol=data['symbol'],
            # qty=data['qty'],
            notional=data['notional'],
            side=data['side'],
            time_in_force=data['time_in_force']
        )
        return order_service.create_order(user_id, order)
    
    
@orders.route('/create-limit-order')
class LimitTradeCreation(Resource):
    @orders.expect(LimitOrder)
    def post(self):
        data = request.json
        user_id = data['user_id']
        limit_order = LimitOrder(
            symbol=data['symbol'],
            limit_price=data['limit_price'],
            notional=data['notional'],
            side=data['side'],
            time_in_force=data['time_in_force']
        )
        return order_service.create_limit_order(user_id, limit_order)
    
    
@orders.route('/get-all-orders')
@api.doc(params={'user_id':'User ID is required'})
class GetAllTrades(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        return order_service.get_all_orders(user_id), 200
    

@orders.route('/cancel-all-orders')
@api.doc(params={'user_id':'User ID is required'})
class CancelAllOrders(Resource):
    def delete(self):
        user_id = request.args.get('user_id')
        return order_service.cancel_all_orders(user_id), 200
    
@orders.route('/cancel-order-by-id')
@api.doc(params={'user_id':'User ID is required', 'order_id':'Order ID is required'})
class CancelOrderByID(Resource):
    def delete(self):
        user_id = request.args.get('user_id')
        order_id = request.args.get('order_id')
        return order_service.cancel_order_by_id(user_id, order_id), 200
    
