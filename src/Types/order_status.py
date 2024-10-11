from enum import Enum

class OrderStatus(Enum):
    ACTIVE
    PARTIALLY_FILLED
    FILLED
    CANCELLED
    ABORTED
