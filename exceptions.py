class BaseError(Exception):
    message = "Неизвестная ошибка"


class NotEnoughSpaceError(BaseError):
    message = "Недостаточно свободных мест"


class ProductNotFound(BaseError):
    message = "Товар не найден"


class NotEnoughProducts(BaseError):
    message = "Недостаточно товара"


class UniqueProductsOutOfRange(BaseError):
    message = "Лимит уникальных товаров исчерпан"


class IncorrectString(BaseError):
    message = "Некорректный формат строки"


class UnknownStorage(BaseError):
    message = "Неизвестный склад"
