"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

n = int(input('Введите n: '))
res_second = 0
i = 0
while i != n:
    i += 1
    res_second += i

res_first = n * (n + 1) / 2

print(f'n(n+1)/2 = ({res_first}) == 1+2+...+n = ({res_second})')


# Решение рекурсивным методом

def calc_sum(n, calc_n=0, res_second=0):
    if calc_n == n:
        return res_second
    else:
        return calc_sum(n, calc_n + 1, res_second + calc_n)


print(f'n(n+1)/2 = ({res_first}) == 1+2+...+n = ({res_second})')
