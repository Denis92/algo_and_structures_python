# 4.	Определить, какое число в массиве встречается чаще всего.
import random

list_input = [random.randint(1, 30) for i in range(100)]
set_count = set(list_input)
print(f'Входной массив чисел {list_input}')
max_repeat = 0
for i in set_count:
    if list_input.count(i) > max_repeat:
        res_num, max_repeat = i, list_input.count(i)
print(f'Чаще всего в массиве встречается число {res_num} ({max_repeat} раз(а))')
