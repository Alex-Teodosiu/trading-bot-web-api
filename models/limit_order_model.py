from models.order_model import Order


class LimitOrder(Order):
    def __init__(self, symbol, notional, side, time_in_force, limit_price):
        super().__init__(symbol, notional, side, time_in_force)
        self.limit_price = limit_price

    def get_limit_price(self):
        return self.limit_price

    def to_dict(self):
        order_dict = super().to_dict()
        order_dict['limit_price'] = self.limit_price
        return order_dict

    def __str__(self):
        return f"LimitOrder({self.symbol}, {self.notional}, {self.side}, {self.time_in_force}, {self.limit_price})"

