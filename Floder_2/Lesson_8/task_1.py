#task_1. Словарь цен.
print("Задание 1")
dict_price: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
product_entry = input("Введите товар ")
if dict_price.get(product_entry)==None:
    print("Такого товара нет")
else:
    print("Цена товара: ", dict_price[product_entry])