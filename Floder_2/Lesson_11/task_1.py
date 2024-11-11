#task_1. Суммирование продаж
print("Задание 1")
#list_price = [100, 200, 300]
list_price = [15, 23, 29, 50]
def sum_sales_with_for(list_price, sum_sales = 0):
    for sale in list_price:
        sum_sales += sale
    return(sum_sales)
sum_sales = sum_sales_with_for(list_price)
print(*list_price, sep = '+', end = f'={sum_sales}')