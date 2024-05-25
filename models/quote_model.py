import datetime

class Quote:
    def __init__(self, ask_exchange, ask_price, ask_size, bid_exchange, bid_price, bid_size, conditions, symbol, tape, timestamp):
        self.ask_exchange = ask_exchange
        self.ask_price = ask_price
        self.ask_size = ask_size
        self.bid_exchange = bid_exchange
        self.bid_price = bid_price
        self.bid_size = bid_size
        self.conditions = conditions
        self.symbol = symbol
        self.tape = tape
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'ask_exchange': self.ask_exchange,
            'ask_price': self.ask_price,
            'ask_size': self.ask_size,
            'bid_exchange': self.bid_exchange,
            'bid_price': self.bid_price,
            'bid_size': self.bid_size,
            'conditions': self.conditions,
            'symbol': self.symbol,
            'tape': self.tape,
            'timestamp': self.timestamp.isoformat() if isinstance(self.timestamp, datetime.datetime) else self.timestamp,
        }
    
    def __str__(self):
        return f"Quote(ask_exchange={self.ask_exchange}, ask_price={self.ask_price}, ask_size={self.ask_size}, bid_exchange={self.bid_exchange}, bid_price={self.bid_price}, bid_size={self.bid_size}, conditions={self.conditions}, symbol={self.symbol}, tape={self.tape}, timestamp={self.timestamp})"
