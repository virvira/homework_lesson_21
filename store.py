from typing import Dict
from constants import STORE_CAPACITY
from base_storage import BaseStorage


class Store(BaseStorage):
    def __init__(self, items: Dict[str, int], capacity: int = STORE_CAPACITY):
        super().__init__(items, capacity)
