#task_3. Отслеживание запасов.
print("Задание 3")
dict_products: dict[str, int] = {'apples': 50, 'bananas': 10, 'cherries': 3}
min_stock = 15
def track_low_stock_with_for(dict_products):
    print('Низкий запас:')
    for product in dict_products:
        if dict_products.get(product) < min_stock:
            print(f'{product} - {dict_products[product]}')

low_quanity = track_low_stock_with_for(dict_products)