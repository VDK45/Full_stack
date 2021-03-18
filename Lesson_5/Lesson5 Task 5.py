"""
    5. Создать (программно) текстовый файл, 
    записать в него программно набор чисел, разделенных пробелами. 
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


with open(f'text_5.txt', 'w', encoding='utf-8') as file:
    text = input('Enter numbers with spaces: ')
    file.write(text)
with open(f'text_5.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split()
    line_int = []
    for i in line:
        line_int.append(int(i)) 
    print(f'Сума чисел {line_int} = {sum(line_int)}')
    
print('----------- Вариант ----------')

file = open(f'sum_numbers.txt', 'w', encoding="utf-8")
line = input('Введите цифры через пробел: ')
file.writelines(line + '\n')
file.close()

file_open = open(f'sum_numbers.txt', 'r', encoding="utf-8")
digit = file_open.readline()
digit = digit.split()

suma = 0
for x in digit:
    suma += int(x)
print(' + '.join(digit), '=', suma)
file_open.close()

print('----------- Вариант ----------')

from random import randint

with open(f'text_5_varian.txt', 'w', encoding='utf-8') as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(' '.join(map(str, my_list))) # запись в файл

print(f'Sum of elements  - {sum(my_list)}')

print('----------- Вариант ок ----------')

from random import randint

with open(f'text_5_varian_2.txt', mode='w+', encoding='utf-8') as file:
    file.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    file.seek(0) #  курсор на начало файла
    print(sum(map(int, file.readline().split())))
