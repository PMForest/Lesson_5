"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

text = input("Enter the text in the new file:\n ")
file = open("task_5.1.txt", "w")
while text:
    file.writelines(text)
    text = input("Enter the text in the new file:\n ")
    if not text:
        break

file.close()

file = open("task_5.1.txt", "r")
content = file.readlines()
print(content)
file.close()

# вар 2

# with open('task_5.1.txt', 'w') as f:
#     while True:
#         line = input('Enter the text in the new file: ')
#         if line == '':
#             break
#         f.write(line + '\n')