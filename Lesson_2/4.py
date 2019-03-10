"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите n: '))
i = 0
res = 1
res_sum = 1
while i != n - 1:
    res = res / -2
    res_sum += res
    i += 1

print(f'Сумма ряда чисел = {res_sum}')


# Решение рекурсивным методом

def calc_sum(n, step=0, res=1, res_sum=1):
    if step == n - 1:
        return f'Сумма ряда чисел = {res_sum}'
    else:
        res /= -2
        return calc_sum(n, step + 1, res, res_sum + res)


print(calc_sum(n))
