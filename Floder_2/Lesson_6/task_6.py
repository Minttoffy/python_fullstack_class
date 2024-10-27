#task_6. Внесение изменений в список товаров.
print("Задание 6")
prod = input ("Ввод продукции: ")
prod = prod.split()
position = int(input("Позиция: "))
name_prod:str = input("Имя товара:")
prod.insert(position, f'{name_prod}')
print(prod)