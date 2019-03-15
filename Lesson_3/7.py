"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random

list_input = [random.randint(0, 100) for i in range(10)]
print(f'Входной массив {list_input}')
min_num_first = min(list_input)
list_input[list_input.index(min_num_first)] = max(list_input)
min_num_second = min(list_input)
print(f'Наименьшие элемент №1 = {min_num_first}\n'
      f'Наименьший элемент №2 = {min_num_second}')
