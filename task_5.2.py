"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

file = open("task_5.2.txt", "r")
content = file.read()
print(f'file contents:\n {content}')

file = open("task_5.2.txt", "r")
content = file.readlines()
print(f'sum of lines in file:\n{len(content)}')

file = open("task_5.2.txt", "r")
content = file.readlines()
for i in range(len(content)):
    print(f'sum symbols in {i + 1} lines: {len(content[i])}')

file = open("task_5.2.txt", 'r')
content = file.read()
content = content.split()
print(f'sum words {len(content)}')
file.close()

"""вар 2"""

# with open('task_5.2.txt') as f:
#     lines = f.readlines()
#     print('Кодичество строк:', len(lines))
#     for num_line, line in enumerate(lines, start=1):
#         print('{} Строка содержит - {} слов'.format(num_line, len(line.split())))






