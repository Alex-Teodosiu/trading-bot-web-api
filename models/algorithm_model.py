class Algorithm:
    def __init__(self, algorithm_name, symbol, user_id, time_stamp):
        self._algorithm_name = algorithm_name
        self._symbol = symbol
        self._user_id = user_id
        self._time_stamp = time_stamp

    def get_algorithm_name(self):
        return self._algorithm_name
    
    def get_symbol(self):
        return self._symbol
    
    def get_user_id(self):
        return self._user_id
    
    def get_time_stamp(self):
        return self._time_stamp

    def to_dict(self):
        return {
            'algorithm_name': self.get_algorithm_name(),
            'symbol': self.get_symbol(),
            'user_id': self.get_user_id(),
            'time_stamp': str(self.get_time_stamp())
        }

    def __str__(self):
        return f"Algorithm Name: {self._algorithm_name}, Symbol: {self._symbol}, User ID: {self._user_id}, Time Stamp: {self._time_stamp}"