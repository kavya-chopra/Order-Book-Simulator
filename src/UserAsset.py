from dataclasses import dataclass
import Asset

@dataclass
class UserAsset:
    asset: Asset
    quantity: int
