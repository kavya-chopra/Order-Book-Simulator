# to be migrated to a database

from enum import Enum
from immutables import Map
# from dataclasses import dataclass

# @dataclass
# class TickerSymbol:
#     name: String
#     asset: AssetType

class TickerSymbolName(Enum):
    GOOGL = 'Google'
    EQIX = 'Equinix'
    OIL = 'Crude Oil'
    BTC = 'Bitcoin'

ticker_symbols = Map({
    TickerSymbolName.GOOGL: AssetType.STOCK,
    TickerSymbolName.EQIX: AssetType.REIT,
    TickerSymbolName.OIL: AssetType.COMMODITY,
    TickerSymbolName.BTC: AssetType.CRYPTOCURRENCY
})
