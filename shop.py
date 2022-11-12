from typing import Dict

from base_storage import BaseStorage
from constants import SHOP_GOODS_MAX_COUNT, SHOP_CAPACITY
from exceptions import UniqueProductsOutOfRange


class Shop(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int = SHOP_CAPACITY):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() < SHOP_GOODS_MAX_COUNT:
            super().add(name, amount)
        else:
            raise UniqueProductsOutOfRange
