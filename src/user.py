import uuid
import UserAsset

class User:

    def __init__(self, funds:int, assets:list[UserAsset]):
        self.id = uuid.uuid1()
        self.funds = funds
        self.assets = assets
