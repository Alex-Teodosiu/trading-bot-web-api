import datetime as dt

class Clock:
    def __init__(self, timestamp, is_open, next_open, next_close):
        self.timestamp = timestamp
        self.is_open = is_open
        self.next_open = next_open
        self.next_close = next_close

    def to_dict(self):
        return {
            'timestamp': self.timestamp.isoformat() if isinstance(self.timestamp, dt.datetime) else self.timestamp,
            'is_open': self.is_open,
            'next_open': self.next_open.isoformat() if isinstance(self.next_open, dt.datetime) else self.next_open,
            'next_close': self.next_close.isoformat() if isinstance(self.next_close, dt.datetime) else self.next_close,
        }

    
    def __str__(self):
        return f"Clock(timestamp={self.timestamp}, is_open={self.is_open}, next_open={self.next_open}, next_close={self.next_close})"
