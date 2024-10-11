import uuid
import datetime

class Order:
    def __init__ (id:uuid, action:OrderAction, status:OrderStatus, timestamp:datetime):
        self.id = uuid.uuid1()
        self.action = action
        self.status = status
        self.timestamp = timestamp