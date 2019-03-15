#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random

list_input = [random.randint(-10, 10) for i in range(10)]
print(f'Входной массив {list_input}')
max_num_negativ = min(list_input)
if max_num_negativ < 0:
    print(f'Максимальное отрицательное число = {max_num_negativ}'
          f'\nИндекс этого числа = {list_input.index(max_num_negativ)} ')
else:
    print('В массиве нет отрицательных чисел')
