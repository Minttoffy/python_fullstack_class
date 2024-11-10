#task_4. Выбор рекламной платформы
print("Задание 4")

def choose_ad_platform(budget):
    if budget > 5000:
        platform = print("Instagram")
        return platform
    elif budget == 5000 or budget > 1000:
        platform = print('Facebook')
        return platform
    else:
        platform = print("Google")
        return platform

budget = int(input("Бюджет: "))
platform = choose_ad_platform(budget)