import uuid

class Asset:

    def __init__(self, id:uuid, asset_type:AssetType, name:String, ticker_symbol:TickerSymbol):
        self.id = uuid.uuid1()
        self.asset_type = asset_type
        self.name = name
        self.ticker_symbol = ticker_symbol
