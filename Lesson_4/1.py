"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile


"""
Задача
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Вывод, разницы во времени выполнения алгоритмов до чисел длинна, которых не привышает 100 цифр нет, 
дальше второй алгоритм работает немного быстрее, но разница во времени не значительна и составляет 0.001 seconds
"""

number = input('Введите число: ')


def first(number):
    number = int(number)
    dec = 1
    count_even = 0
    count_odd = 0
    while number % dec != number:
        dec *= 10
        if (int((number % dec) // (dec / 10))) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


def second(number):
    number = list(number)
    count_even = len([i for i in number if int(i) % 2 == 0])
    count_odd = len([i for i in number if int(i) % 2 != 0])
    return count_even, count_odd


cProfile.run('first(number)')
cProfile.run('second(number)')


"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Вывод, нерекурсивный алгоритм работает быстрее + прибольших n нехватает глубины рекурсии
"""

import sys
sys.setrecursionlimit(20000)

n = int(input('Введите n: '))
def first_s(n):
    i = 0
    res = 1
    res_sum = 1
    while i != n - 1:
        res = res / -2
        res_sum += res
        i += 1

def calc_sum(n, step=0, res=1, res_sum=1):
    if step == n - 1:
        return f'Сумма ряда чисел = {res_sum}'
    else:
        res /= -2
        return calc_sum(n, step + 1, res, res_sum + res)

cProfile.run('first_s(n)')
cProfile.run('calc_sum(n)')



"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
 Вывод, нерекурсивный алгоритм работает быстрее + прибольших n нехватает глубины рекурсии
"""
n = int(input('Введите n: '))
def first_f(n):
    res_second = 0
    i = 0
    while i != n:
        i += 1
        res_second += i

    res_first = n * (n + 1) / 2

    return f'n(n+1)/2 = ({res_first}) == 1+2+...+n = ({res_second})'


# Решение рекурсивным методом
def calc_sum_s(n, calc_n=0, res_second=0):
    if calc_n == n:
        return res_second
    else:
        return calc_sum(n, calc_n + 1, res_second + calc_n)

cProfile.run('first_f(n)')
cProfile.run('calc_sum_s(n)')

"""
    Задача. Вычисление факториала
    Оба алгоритма решают поставленную задачу примерно за одно и то же время    
"""
n = int(input('Введите n: '))

def first_metod(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def recur_metod(n):
    if n == 0:
        return 1
    else:
        return recur_metod(n - 1) * n

cProfile.run('first_metod(n)')
cProfile.run('recur_metod(n)')

