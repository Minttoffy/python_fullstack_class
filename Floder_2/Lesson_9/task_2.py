#task_2. Преобразование RGB в HEX.
print("Задание 2")
def convert_to_hex(red, green, blue):
    red_hex = hex(red)
    green_hex = hex(green)
    blue_hex = hex(blue)
    res = map(str, [red_hex.removeprefix("0x").zfill(2), green_hex.removeprefix("0x").zfill(2), blue_hex.removeprefix("0x").zfill(2)])
    return ''.join(res)

rgb_input = input("Введите число RGB через запятую 3 раза: ").split(", ")
red = int(rgb_input[0])
green = int(rgb_input[1])
blue = int(rgb_input[2])
res = convert_to_hex(red, green, blue)
print('#',(res.upper()))