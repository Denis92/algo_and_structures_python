"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import cProfile


def first(n):
    list_num = [i for i in range(2, n)]
    len_list = len(list_num)
    for i in list_num:
        for j in range(len_list):
            if list_num[j] > 0 and i > 0 and list_num[j] != i:
                if list_num[j] % i == 0:
                    list_num[j] = 0
    return list_num


# Алгоритм «Решето Эратосфена»

def second(n):
    list_num_second = [i for i in range(2, n)]
    len_list = len(list_num_second)
    for i in list_num_second:
        p = i
        if p ** 2 > len_list:
            break
        elif p == 0:
            continue
        else:
            for j in range(2, len_list):
                temp = p * j
                if temp in list_num_second:
                    list_num_second[temp - 2] = 0
    return list_num_second


n = 10000

cProfile.run('first(n)')
cProfile.run('second(n)')

"""
Представленный Алгоритм «Решето Эратосфена» работает гораздо медленнее, чем первый
при n = 10000 Первый алгоритм выполняется за 6 секунд, а второй за 36 секунд
"""
