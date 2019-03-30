"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
В результате работы над этим заданием, был реализована своя функция для сортировки пузырёк(изнаально я не подсматривал
в код, который писал преподаватель) В двльнейшем я сравнил две реализации в итоге выяснилось, что реализация
преподавателя работает быстрее
"""
import random
import copy
import time

list_input = [random.randint(-100, 100) for i in range(10)]
print(list_input)


def time_count(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        finisf = time.time()
        print(f'Время выполнения функции {func.__doc__} = {finisf - start}.с')
        return res

    return wrapper


@time_count
def my_bubble_sort(input_list):
    """
    Сортировка пузырёк реализованная мной
    """
    i = 1
    count = 0
    temp_list = input_list.copy()
    while count < len(input_list):
        count += 1
        if i >= len(input_list):
            if temp_list == input_list:
                break
            else:
                temp_list = input_list.copy()
        for i in range(1, len(input_list)):
            if input_list[-i] > input_list[-i - 1]:
                input_list[-i], input_list[-i - 1] = input_list[-i - 1], input_list[-i]
    return input_list


@time_count
def bubble_sort(orig_list):
    """
    Сортировка пузырёк реализованная преподавателем
    """
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] > orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list


print(my_bubble_sort(list_input))
print(bubble_sort(list_input))
