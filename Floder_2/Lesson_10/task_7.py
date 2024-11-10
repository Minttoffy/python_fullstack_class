#task_7. Расчет скидок
print("Задание 7")
#orders_list = [1000, 2000, 3000, 5000, 10000, 15000, 100, 200, 300, 400, 50, 100]
input_orders = input('Введите числа через запятую: ').split(', ')
orders = [float(x) for x in input_orders]

def calculate_discond(orders, index = 0, order = None):
    finished = []
    if index < len(orders):
        first_order = orders[index]
        first_discount = order * 0.1 if order is not None else 0
        disicounted_price = first_order - first_discount if first_discount is not None else first_discount
        finished.append(disicounted_price)
        finished += calculate_discond(orders, index + 1, first_order)
        return finished
    else:
        return finished
res = [int(x) for x in calculate_discond(orders)]
print(f'Цены со скидками: {res}')