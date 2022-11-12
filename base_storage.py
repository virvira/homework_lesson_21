from typing import Dict

from abstract_storage import AbstractStorage
from exceptions import NotEnoughSpaceError, NotEnoughProducts, ProductNotFound


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.items = items
        self.capacity = capacity

    def get_items(self) -> Dict[str, int]:
        return self.items

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            raise NotEnoughSpaceError

        if name not in self.items:
            self.items[name] = amount
        else:
            self.items[name] += amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self.items:
            raise ProductNotFound

        if self.items[name] >= amount:
            self.items[name] -= amount
            if self.items[name] == 0:
                self.items.pop(name)
        else:
            raise NotEnoughProducts

    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())

    def get_unique_items_count(self) -> int:
        return len(list(self.items.keys()))
