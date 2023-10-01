# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


def fill_backpack(items, max_weight):
    sorted_items = sorted(items.items(), key=lambda x: x[1])
    backpack = {}
    total_weight = 0

    for item, weight in sorted_items:
        if total_weight + weight <= max_weight:
            backpack[item] = weight
            total_weight += weight

    return backpack

items = {
    'Тент': 2,
    'Спальник': 1,
    'Еда': 3,
    'Вода': 2,
    'Кружка': 0.5
}
max_weight = 5
result = fill_backpack(items, max_weight)
print(result)