import uuid
from Types import AssetType
import TickerSymbol

class Asset:

    def __init__(self, asset_type:AssetType, name:str, ticker_symbol:TickerSymbol):
        self.id = uuid.uuid1()
        self.asset_type = asset_type
        self.name = name
        self.ticker_symbol = ticker_symbol
