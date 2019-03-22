"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple
import cProfile


class CompanyInfo:
    company_list = namedtuple('Company', 'company_name company_profit sum_profit')
    input_company = company_list(
        company_name=[],
        company_profit=[],
        sum_profit=[],
    )

    more_middle = 0
    under_middle = 0
    middle_profit = 0

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def company(self):
        for i in range(self.quantity):
            self.input_company.company_name.append(input('Введите название предприятия: '))
            list_profit = list(map(float, input('Введите прибыль за каждый квартал через пробел: ').split(' ')))
            self.input_company.company_profit.append(list_profit)
            self.input_company.sum_profit.append(sum(self.input_company.company_profit[i]))

    def calc_middle_profit(self):
        self.company()
        self.middle_profit = sum(self.input_company.sum_profit) / quantity
        self.more_middle = list(filter(lambda x: x > self.middle_profit, self.input_company.sum_profit))
        self.under_middle = list(filter(lambda x: x < self.middle_profit, self.input_company.sum_profit))

    def print_company_more_middle(self):
        self.calc_middle_profit()
        list_company = [self.input_company.company_name[self.input_company.sum_profit.index(i)]
                        for i in self.more_middle]
        return print(f'Название предприятия(й) прибыль которых выше среднего( {self.middle_profit}) : '
                     f'{", ".join(list_company)}')

    def print_company_under_middle(self):
        list_company = [self.input_company.company_name[self.input_company.sum_profit.index(i)]
                        for i in self.under_middle]
        return print(f'Название предприятия(й) прибыль которых ниже среднего( {self.middle_profit}) : '
                     f'{", ".join(list_company)}')


quantity = int(input('Введите количество предприятий: '))
my_company_list = CompanyInfo(quantity)

cProfile.run('my_company_list.print_company_more_middle()')
cProfile.run('my_company_list.print_company_under_middle()')
