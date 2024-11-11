#task_2. Подсчет определенных товаров.
print("Задание 2")
#product = ['fruit', 'toy', 'fruit', 'toy']
#input_product = 'toy'
product = ['clothes', 'clothes', 'clothes']
input_product = 'clothes'
def count_specific_items_with_while(product, num_product = 0):
    while input_product in product:
        num_product += product.count(input_product)
        return num_product
        break
    else:
        print('Данный товар отсутствует')
num_product = count_specific_items_with_while(product)
print('Количество продуктов: ', num_product)