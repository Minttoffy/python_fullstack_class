#task_3. Элементы подсписка
print("Задание 3")
ent_list = input('Введите числа от 3 и более: ').split(',')
num_list = [int(i) for i in ent_list]
k = num_list[1]
n = num_list[0]
m = num_list[-1]
print(f'Числа из заданного подсписка: {num_list[n:m:k]}')