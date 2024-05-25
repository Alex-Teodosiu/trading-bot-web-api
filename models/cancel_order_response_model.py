class CancelOrderResponse:
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status
        }
    
    def __str__(self):
        return f"id: {self.id}, status: {self.status}"
