#task_3. Минимальная и максимальная цена
print("Задание 3")
dict_price: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
price_min = dict_price.get(min(dict_price, key = dict_price.get))
price_max = dict_price.get(max(dict_price, key = dict_price.get))
price = list(dict_price.values())
products = list(dict_price.keys())
name = products[price.index(price_min)]
name2 = products[price.index(price_max)]
print(f'Самый дешевый товар: {name} за {price_min} рублей \nСамый дорогой товар: {name2} за {price_max} рублей')