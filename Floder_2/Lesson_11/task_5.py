#task_5. Расписание продаж
print("Задание 5")
num = int(input("Ввод максимального числа в месяце: "))
def sales_schedule_with_range(num):
    low_quanity = list(range(3, num + 1, 3))
    print("Дни распродаж:", low_quanity)
low_quanity = sales_schedule_with_range(num)