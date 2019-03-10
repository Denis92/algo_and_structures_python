"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

i = 32
res_str = ''
count_str = 0
while i != 128:
    res_str += f'код-({i})---символ-({chr(i)})  |'
    if count_str == 10:
        print(res_str)
        res_str = ''
        count_str = 0
    else:
        count_str += 1
    i += 1
print(res_str)

print('\n\n')


# Решение рекурсивным методом
def print_table(start_symbol, res_str='', count_str=0):
    if start_symbol == 128:
        return print(res_str)
    else:
        res_str += f'код-({start_symbol})---символ-({chr(start_symbol)})  |'
        if count_str == 10:
            print(res_str)
            res_str = ''
            count_str = 0
        else:
            count_str += 1
        return print_table(start_symbol + 1, res_str, count_str)


print_table(32)
