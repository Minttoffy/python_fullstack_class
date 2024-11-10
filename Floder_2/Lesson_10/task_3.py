#task_3. Ответственный сотрудник
print("Задание 3")
task_ratio_dict: dict[str, int] = {'Анна': 5, 'Боб': 7, 'Сюзан': 9}
#task_ratio_dict:dict[str, int] = { 'Джон': 1,  'Майк': 1, "Эмили": 1}

def most_responsible (task_ratio_dict):
    val_task = list(task_ratio_dict.values())
    max_ratio = max(val_task)
    responsible_worker = [name for name, complected in task_ratio_dict.items() if complected == max_ratio]
    return responsible_worker

responsible_worker = most_responsible (task_ratio_dict)
res = ', '.join(map(str, responsible_worker))
print("Самый ответственный сотрудник: ", res)