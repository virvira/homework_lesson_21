from abc import ABC
from typing import Dict

from abstract_storage import AbstractStorage
from exceptions import IncorrectString, UnknownStorage


class Request(ABC):
    def __init__(self, storages: Dict[str, AbstractStorage], request: str):
        request_args = request.split()
        if len(request_args) != 7 or not request_args[1].isdigit():
            raise IncorrectString

        self._from = request_args[4]
        self.to = request_args[6]
        self.amount = int(request_args[1])
        self.product = request_args[2]

        if self._from not in storages or self.to not in storages:
            raise UnknownStorage

    def get_from(self):
        return self._from

    def set_from(self, value):
        self._from = value

    def get_to(self):
        return self.to

    def set_to(self, value):
        self.to = value

    def get_amount(self):
        return self.amount

    def set_amount(self, value):
        self.amount = value

    def get_product(self):
        return self.product

    def set_product(self, value):
        self.product = value
