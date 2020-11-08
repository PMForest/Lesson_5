"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open('task_5.5.txt', 'w+') as file:
    number = input('enter numbers separated by spaces:\n')
    file.writelines(number)
    new_num = number.split()

    print(sum(map(int, new_num)))

# вар 2

# with open('5.txt', 'w') as f:
#     nums = input('Введите целые числа через пробел: ')
#     f.write('Выведенные числа: ' + nums + '\n')
#     nums = map(int, nums.split())  # without list
#     sum_nums = sum(nums)
#     f.write('Сумма чисел: ' + str(sum_nums))
#     print('Сумма введенных чисел:', sum_nums)
# print('Все записанно в файл')
