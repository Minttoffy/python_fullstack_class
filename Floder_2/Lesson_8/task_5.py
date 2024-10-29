#task_5. Уникальные товары для двух магазинов.
print("Задание 5")
first_list_products_input = set(input("Введите названия товаров в первом магазине: ").split(', '))
two_list_products_input = set(input("Введите названия товаров во втором магазине: ").split(', '))
print(f'Только в первом магазине: {first_list_products_input.difference(two_list_products_input)}')
print(f'Только во втором магазине: {two_list_products_input.difference(first_list_products_input)}')