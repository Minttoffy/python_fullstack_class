#task_8. Перестановка товаров.
print("Задание 8")
prod:tuple[str] = input("Ввод продуктов: ").split(", ")
a, b = map(int, input("Ввод чисел ").split(", "))
clear = []
if a==1:
    if b==len(prod):
        a-=1
        b-=1
        clear.append(prod[b])
        clear.append(prod[a-b])
        clear.append(prod[a])
        print(clear)
    else:
        print("Значения либо больше, либо меньше чем в задании")