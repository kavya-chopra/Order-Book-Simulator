import uuid

class Asset:

    def __init__(self, id:uuid, type:Type, name:String, ticker_symbol:TickerSymbol):
        self.id = uuid.uuid1()
        self.type = type
        self.name = name
        self.ticker_symbol = ticker_symbol
