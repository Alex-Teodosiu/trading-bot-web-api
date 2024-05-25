
class Order:
    def __init__(self, symbol, notional, side, time_in_force):
        self.symbol = symbol
        # self.qty = qty
        self.notional = notional
        self.side = side
        self.time_in_force = time_in_force

    def get_symbol(self):
        return self.symbol

    # def get_qty(self):
    #     return self.qty
    
    def get_notional(self):
        return self.notional

    def get_side(self):
        return self.side

    def get_time_in_force(self):
        return self.time_in_force

    def to_dict(self):
        return {
            'symbol': self.symbol,
            #'qty': self.qty,
            'notional': self.notional,
            'side': self.side,
            'time_in_force': self.time_in_force,
        }

    def __str__(self):
        return f"Order({self.symbol}, {self.notional}, {self.side}, {self.time_in_force})"
