#task_1. Скидки в магазине
print("Задание 1")
price = int(input('Ввелите цену: '))
visits = int(input('Количество посещений: '))
if visits >= 20:
    price -= (20*price/100)
    print('Текущая цена: ', price)
elif visits >= 10:
    price -= price/10
    print('Текущая цена: ', price)
else:
    print('Текущая цена: ', price)