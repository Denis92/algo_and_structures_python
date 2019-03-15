# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

list_input = [[random.randint(0, 100) for i in range(5)] for j in range(5)]
print(f'Входной массив {list_input}')
list_temp = [list_input[i][j] for j in range(0, len(list_input[0])) for i in range(0, len(list_input))]
step = int(len(list_temp) / len(list_input))
list_min = [min(list_temp[i * step:i * step + step]) for i in range(0, step)]

print(f'Максимальный элемент из минимальных элементов столбцов матрицы = {max(list_min)}')