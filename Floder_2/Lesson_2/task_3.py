#task_3. Расчет объема товаров.
print("Задание 3")
books = int(input("Введите количество книг: "))
goods = int(input("Введите количество товаров: "))
toys = int(input("Введите количество игрушек: "))
num_volue = books*2 + goods*1.5 + toys*3
print("Общий объем:", num_volue, "м^3")