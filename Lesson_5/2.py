"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HexOperation:
    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    def __add__(self, other):
        return list(hex(int(''.join(self.num_first), 16) + int(''.join(other.num_second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(other.num_second), 16)))[2:]


hex_num_first = list(input('Введите первое шеснадцатиричное число: '))
hex_num_second = list(input('Введите второе шеснадцатиричное число: '))

res_sum = HexOperation(hex_num_first, hex_num_second) + HexOperation(hex_num_first, hex_num_second)
res_mul = HexOperation(hex_num_first, hex_num_second) * HexOperation(hex_num_first, hex_num_second)
print(f'Сумма чисел = {res_sum}\nПроизведение чисел = {res_mul}')
