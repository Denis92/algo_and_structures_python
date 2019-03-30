"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
К моему сожалению, я не успел написать свою функцию для алгоритма слияния, однако постарался разобрать предоставленную
на уроке
"""

import timeit
import random
orig_list = [random.randint(0, 50) for i in range(10)]
print(orig_list)
def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]
        print(f'{left}   {right}')

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1

            else:
                orig_list[k] = right[j]
                j += 1
            print(f'orig {orig_list}')
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1
            print(f'orig_end {orig_list}')

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list

# замеры
print(merge_sort(orig_list))
print(timeit.timeit("merge_sort(orig_list)",
    setup="from __main__ import merge_sort, orig_list", number=10))
