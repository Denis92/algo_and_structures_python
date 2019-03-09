"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

i = 32
print('код | символ')
while i != 127:
    print(f'{i}  |  "{chr(i)}"')
    i += 1

print('код | символ')


# Решение рекурсивным методом
def print_table(start_symbol):
    if start_symbol == 127:
        return 1
    else:
        print(f'{start_symbol}  |  "{chr(start_symbol)}"')
        start_symbol += 1
        return print_table(start_symbol)


print_table(32)
