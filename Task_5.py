# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

lst = [1, 2, 3, 1, 2]
result = find_duplicates(lst)
print(result)