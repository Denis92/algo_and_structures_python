"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
list_number = input('Введите последовательность чисел: ')
number = input('Введите цифру, которую необходимо посчитать: ')
count_number = 0
for i in list_number:
    if i == number:
        count_number += 1

print(f'Искомая цифра {number} повторяется {count_number} раз(а)')


