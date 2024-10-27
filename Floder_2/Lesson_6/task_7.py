#task_7. Удаление товаров.
print("Задание 7")
prod = input ("Ввод продукции: ")
prod = prod.split()
position = int(input("Позиция: "))
prod.pop(position)
print(prod)