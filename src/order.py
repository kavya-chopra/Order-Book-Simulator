import uuid
import datetime
from Types import OrderAction, AssetType, OrderType, OrderStatus

class Order:

    def __init__(self, action:OrderAction, units:float, price:float, asset:AssetType, order_type:OrderType):
        self.id = uuid.uuid1()
        self.action = action
        self.units = units
        self.price = price
        self.asset = asset
        self.order_type = order_type
        self.status = OrderStatus.ACTIVE
        self.amount_filled = 0
        self.timestamp = datetime.now()
