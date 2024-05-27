class Algorithm:
    def __init__(self, algorithm_name, symbol, user_id, time_stamp):
        self.algorithm_name = algorithm_name
        self.symbol = symbol
        self.user_id = user_id
        self.time_stamp = time_stamp

    def get_algorithm_name(self):
        return self.algorithm_name
    
    def get_symbol(self):
        return self.symbol
    
    def get_user_id(self):
        return self.user_id
    
    def get_time_stamp(self):
        return self.time_stamp

    def to_dict(self):
        return {
            'algorithm_name': self.get_algorithm_name(),
            'symbol': self.get_symbol(),
            'user_id': self.get_user_id(),
            'time_stamp': str(self.get_time_stamp())
        }

    def __str__(self):
        return f"Algorithm Name: {self.algorithm_name}, Symbol: {self.symbol}, User ID: {self.user_id}, Time Stamp: {self.time_stamp}"