#task_1. Подсчет скидки
print("Задание 1")
price_list = input("Введите цены через запятую и в конце скидку числом без процентов: ").split(", ")
price_and_action = [int(i) for i in price_list]
def calculate_discount(sum_price, action):
    res:int = sum_price//action
    return res
sum_price = sum(price_and_action[0:-1])
action = price_and_action[-1]
res = calculate_discount(sum_price, action)
print(res)