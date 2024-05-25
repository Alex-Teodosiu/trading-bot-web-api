class OrderResponse:
    def __init__(self, id, client_order_id, created_at, updated_at, submitted_at, filled_at, expired_at, canceled_at, failed_at, 
                 replaced_at, replaced_by, replaces, asset_id, symbol, asset_class, notional, qty, filled_qty, filled_avg_price, 
                 order_class, order_type, type, side, time_in_force, limit_price, stop_price, status, extended_hours, legs, 
                 trail_percent, trail_price, hwm):
        self.id = id
        self.client_order_id = client_order_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.submitted_at = submitted_at
        self.filled_at = filled_at
        self.expired_at = expired_at
        self.canceled_at = canceled_at
        self.failed_at = failed_at
        self.replaced_at = replaced_at
        self.replaced_by = replaced_by
        self.replaces = replaces
        self.asset_id = asset_id
        self.symbol = symbol
        self.asset_class = asset_class
        self.notional = notional
        self.qty = qty
        self.filled_qty = filled_qty
        self.filled_avg_price = filled_avg_price
        self.order_class = order_class
        self.order_type = order_type
        self.type = type
        self.side = side
        self.time_in_force = time_in_force
        self.limit_price = limit_price
        self.stop_price = stop_price
        self.status = status
        self.extended_hours = extended_hours
        self.legs = legs
        self.trail_percent = trail_percent
        self.trail_price = trail_price
        self.hwm = hwm
        # self.subtag = subtag
        # self.source = source

    def to_dict(self):
        return {
            'id': self.id,
            'client_order_id': self.client_order_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'submitted_at': self.submitted_at,
            'filled_at': self.filled_at,
            'expired_at': self.expired_at,
            'canceled_at': self.canceled_at,
            'failed_at': self.failed_at,
            'replaced_at': self.replaced_at,
            'replaced_by': self.replaced_by,
            'replaces': self.replaces,
            'asset_id': self.asset_id,
            'symbol': self.symbol,
            'asset_class': self.asset_class,
            'notional': self.notional,
            'qty': self.qty,
            'filled_qty': self.filled_qty,
            'filled_avg_price': self.filled_avg_price,
            'order_class': self.order_class,
            'order_type': self.order_type,
            'type': self.type,
            'side': self.side,
            'time_in_force': self.time_in_force,
            'limit_price': self.limit_price,
            'stop_price': self.stop_price,
            'status': self.status,
            'extended_hours': self.extended_hours,
            'legs': self.legs,
            'trail_percent': self.trail_percent,
            'trail_price': self.trail_price,
            'hwm': self.hwm,
            # 'subtag': self.subtag,
            # 'source': self.source
        }

    def __str__(self):
        return str(self.to_dict())
