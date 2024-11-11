#task_4. Перевод единиц измерения.
print("Задание 4")
fr_metres = ([1, 2], 'meters')
def convert_units_with_while(fr_metres):
    num = 0
    metr = fr_metres[num]
    while num < len(metr):
        print(f'{metr[num]} {fr_metres[1]}(s) = {metr[num] * 3.28084} foot (feet), {num}')
        num += 1
        print(f'{metr[num]} {fr_metres[1]}(s) = {metr[num] * 3.28084} foot (feet), {num}')
        break
conversion = convert_units_with_while(fr_metres)