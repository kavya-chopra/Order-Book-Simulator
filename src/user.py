import uuid

class User:

    def __init__(self, id:uuid, funds:int, assets:dict[Asset, int]):
        self.id = uuid.uuid1()
        self.funds = funds
        self.assets = assets
