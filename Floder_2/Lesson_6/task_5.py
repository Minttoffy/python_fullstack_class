#task_5. Обмен цен (сменить первую на последнюю)
print("Задание 5")
price = input ("Ввод цен: ")
act = price.split()
act.insert(0, max(act))
act.pop()
act.insert(1, max(act))
act.pop(1)
print(' '.join(act))