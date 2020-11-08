"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

file = open("task_5.3.txt", "r")
content = file.read()
print(f'file contents:\n {content}')


with open('task_5.3.txt', 'r') as my_file:
    minimum = []
    sred = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            minimum.append(i[0])
        sred.append(i[1])
print(f'salary less 20.000 {minimum}, average income {sum(map(int,sred)) / len(sred)}')

"""вар 2 """ #будет работать только с разделителев " - "

# with open('task_5.3.txt') as f:
#     salaries = []
#     lines = f.readlines()
#     for line in lines:
#         name, salary = line.split(' - ')
#         salaries.append(int(salary))
#         if int(salary) < 20000:
#             print(line, end='')
#     print('\nsalary less 20.000:', sum(salaries) / len(salaries))