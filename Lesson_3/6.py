"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

list_input = [random.randint(-10, 10) for i in range(100)]
print(f'Входной массив {list_input}')
max_pos = list_input.index(max(list_input))
min_pos = list_input.index(min(list_input))
print(f'Сумма элементов находящихся между минимальным {min(list_input)} и максимальным {max(list_input)} элементами'
      f' = {sum(list_input[min_pos + 1: max_pos])}')

# Второй вариант.
if max_pos > min_pos:
    print(f'Сумма элементов находящихся между минимальным {min(list_input)} и максимальным {max(list_input)} элементами'
          f' = {sum(list_input[min_pos + 1: max_pos])}')
else:
    print(f'Сумма элементов находящихся между максимальным {max(list_input)} и минимальным {min(list_input)} элементами'
          f' = {sum(list_input[max_pos + 1: min_pos])}')
