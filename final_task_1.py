import logging


def fill_backpack(items, max_weight):
    sorted_items = sorted(items.items(), key=lambda x: x[1])
    backpack = []
    total_weight = 0

    for item, weight in sorted_items:
        if total_weight + weight <= max_weight:
            backpack.append(item)
            total_weight += weight
        else:
            logging.info(f"Вещь '{item}' не помещается в рюкзак.")

    return backpack
    # если масса текущей вещи позволяет ее добавить в рюкзак без превышения
    # максимальной грузоподъемности, тогда добавляем ее в рюкзак. если вещь не помещается -
    # записываем в лог.


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Запуск программы для комплектации рюкзака."
    )
    parser.add_argument(
        "--max_weight", type=int, help="Максимальная грузоподъемность рюкзака"
    )
    args = parser.parse_args()

    items = {"Тент": 2, "Спальник": 1, "Еда": 3, "Вода": 2, "Кружка": 0.5}

    max_weight = args.max_weight or 5
    # запуск из командной строки с передачей параметра  --max_weight
    # для задания максимальной грузоподъемности рюкзака. если параметр не передан,
    # используем значение по умолчанию - 5 у.е.

    logging.basicConfig(level=logging.INFO)

    result = fill_backpack(items, max_weight)
    logging.info(f"Комплектация рюкзака: {result}")
