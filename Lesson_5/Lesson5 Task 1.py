"""
    1. Создать программно файл в текстовом формате, 
    записать в него построчно данные, 
    вводимые пользователем. 
    Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open('test_text.txt', 'w', encoding="utf-8")
line = ' '
while line:
    line = input("Input new string: ")
    my_file.write(f"{line}\n") if line != '' else my_file.close()
# открываем созданый файл и читаем:
file = open('test_text.txt', 'r')
content = file.read()
print(content)
file.close()

#-------------
with open(f'test_text_1.txt', 'w', encoding="utf-8") as f:
    while True:
        line = input('Input new string or empty string to done: ')
        if not line:
            break
        f.write(f"{line}\n") # писать 1ый раз
        print(line, file=f) # второй раз 
# открываем созданый файл и читаем:
file = open('test_text_1.txt', 'r')
content = file.read()
print(content)
file.close()

#-------------
print('Введите текст: ')
with open(f'test_text_2.txt', 'w', encoding="utf-8") as my_file:
    while (line := input()) != '' :
        my_file.write(f"{line}\n")
# открываем созданый файл и читаем:
file = open('test_text_2.txt', 'r')
content = file.read()
print(content)
file.close()

#-------------
file = open(f'test_text_3.txt', 'w', encoding="utf-8")
line = input('Введите текст: ')
while line:
    file.writelines(line + '\n')
    line = input('Введите текст: ')
    if not line:
        break

file.close()
print('-' * 9, 'открываем созданый файл и читаем:', '-' * 9)
# открываем созданый файл и читаем:
file = open('test_text_3.txt', 'r')
content = file.read()
print(content)
file.close()


