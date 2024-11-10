#task_6. Поиск максимального элемента.
print("Задание 6")
def find_max_price (list_price):
    list_price.sort()
    return list_price
list_price = []
list_input = list(map(int, input('Введите числа через запятую: ').split(', ')))
list_price.extend(list_input)
list_price = find_max_price(list_price)
print(list_price[-1])