"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
                                                                                            в новый текстовый файл."""
translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_task = []

with open('task_5.4.txt', 'r') as new_file:
    for i in new_file:
        i = i.split(' ', 1)
        new_task.append(translate[i[0]] + ' ' + i[1])
    print(new_task)

with open("task_5.4_new.txt", "w") as new_file:
    new_file.writelines(new_task)




# вар 2

with open('task_5.4.txt', encoding='utf-8') as f:
    lines = f.readlines()


with open('task_5.4_new.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)
