#task_2.Скидки на товары (вывести не четные)
print("Задание 2")
price:int = input ("Ввод цен: ")
action = price.split()
print(' '.join(action[1::2]))