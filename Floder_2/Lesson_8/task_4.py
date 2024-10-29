#task_4. Управление персоналом
print("Задание 4")
"""post_workers:dict[str,str,str] = ([("Снабжение", "Менеджер", "Иванов"), ("Дизайн", "Дизайнер", "Смирнов"),
                       ("Снабжение", "Менеджер", "Петров"), ("Дизайн","Иллюстратор", "Сидоров")
                       ("Маркетинг", "Аналитик", "Сергеев"), ("Дизайн", "Дизайнер", "Васильев")])"""
suply = {}
design = {}
market = {}
for i in range (6):
    worker_list = input("Введите Отдел, Должность, Фамилию нового работника: ").split(', ')
    if worker_list[0] == "Снабжение":
        suply.update({worker_list[1] : worker_list[2]})
        print(suply)
    elif worker_list[0] == "Дизайн":
        design.update({worker_list[1] : worker_list[2]})
    elif worker_list[0] == "Маркетинг":
        market.update({worker_list[1] : worker_list[2]})
    else:
        print("Вы ввели отдел которого нет в задании (есть 3 отдела - Снабжение, Дизайн, Маркетинг).")
print(f"Снабжение : {suply}")
print(f"Дизайн: {design}")