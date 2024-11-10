#task_5.Комплексный анализ эффективности рекламы.
print("Задание 5")
def analyze_ad_efficiency(click, show, view):
    if click/show > 0.1:
        efficiency = print('Высокая')
        return efficiency
    elif 0.1 > click / show >= 0.05 and click < view:
        efficiency = print('Средняя')
        return efficiency
    elif 0.05 > click / show >= 0.01:
        efficiency = print('Низкая')
        return efficiency
    elif click / show < 0.01 and view > show:
        efficiency = print('Недооцененная')
        return efficiency
    else:
        efficiency = print('Неопределенная')
        return efficiency
click, show, view = map(int, input('Клики, Показы, Просмотры: ').split(', '))
efficiency = analyze_ad_efficiency(click, show, view)
