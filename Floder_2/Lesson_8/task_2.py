#task_2. Синонимы в дизайне 
print("Задание 2")
synonyms_dict: dict[str, str] = {'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'}
words_entry = input('Ввод слова: ')
if synonyms_dict.get(words_entry)==None:
    print("Такого слова пока ещё нет")
else:
    print("Синоним к слову: ", synonyms_dict[words_entry])