"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
                                                                               форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

firm = {}
form = {}
summa = 0
cost = 0
average = 0

with open('task_5.7.txt') as file:
    for line in file:
        name, name_2, earnung, cost_2 = line.split()
        firm[name] = int(earnung) - int(cost_2)
        if firm.setdefault(name) >=0:
            summa = summa + firm.setdefault(name)
            average += 1
    if average != 0:
        summa_all = summa / average
        print(f'Average profit - {summa_all:.2f}')
    else:
        print(f'Average profit - income loss')
    form = {'Average profit': round(summa_all)}
    firm.update(form)
    print(f'profit of each company - {firm}')

with open('task_5.7.json', 'w') as file_json:
    json.dump(firm, file_json)

    js_str = json.dumps(firm)
    print(f'json file created: \n '
          f'{js_str}')


# вар 2

# import json
#
# firm_dict = {}
# average_profit = []
# with open('task_5.7.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         name, form, revenue, costs = line.split()
#         profit = int(revenue) - int(costs)
#         firm_dict[name] = profit
#         if profit > 0:
#             average_profit.append(profit)
#
# average_profit = sum(average_profit) / len(average_profit)
# out_info = [firm_dict, {'average_profit': average_profit}]
#
# with open('task_5.7.json', 'w') as f_json:
#     json.dump(out_info, f_json)
#
# with open('task_5.7.json') as f_json:
#     print(json.load(f_json))