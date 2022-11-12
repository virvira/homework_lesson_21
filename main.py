from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store

shop = Shop(
    items={
        "печеньки": 3,
        "коробочки": 7,
        "собачки": 1
    },
)

store = Store(
    items={
        "печеньки": 18,
        "коробочки": 27,
        "собачки": 10
    },
)

storages = {
    "магазин": shop,
    "склад": store
}

if __name__ == '__main__':
    while True:
        # Вывод содержимого складов
        for item in storages:
            print(f"В {item} хранится {storages[item].get_items()}")

        # Запрос ввода пользователя
        print("Введите строку в формате 'Доставить 3 собачки из склад в магазин'\n"
              "Введите 'stop' или 'стоп', чтобы выйти")
        user_input = input()

        if user_input == "stop" or user_input == 'стоп':
            break

        try:
            request = Request(storages=storages, request=user_input)
            destination = request.get_to()
            departure = request.get_from()

            storages[departure].remove(name=request.get_product(), amount=request.get_amount())
            print(f"Курьер забрал {request.get_amount()} {request.get_product()} с {request.get_from()}")
            print(f"Курьер везет {request.get_amount()} {request.get_product()} с {request.get_from()} в {request.get_to()}")

            storages[destination].add(name=request.get_product(), amount=request.get_amount())
            print(f"Курьер доставил {request.get_amount()} {request.get_product()} в {request.get_to()}")
        except BaseError as error:
            print(error.message)
