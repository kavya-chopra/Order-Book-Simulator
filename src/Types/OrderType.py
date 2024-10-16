from enum import Enum

class OrderType(Enum):
    LIMIT
    MARKET
    FILL_OR_KILL
