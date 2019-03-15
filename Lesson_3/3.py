# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random

list_randint = [random.randint(1, 100) for i in range(1, 10)]
print(f'Исходный массив {list_randint}')
max_num = max(list_randint)
min_num = min(list_randint)
max_pos = list_randint.index(max_num)
min_pos = list_randint.index(min_num)
list_randint[max_pos], list_randint[min_pos] = min_num, max_num
print(f'Итоговый массив {list_randint}')
