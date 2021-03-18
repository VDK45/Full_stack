"""
    6. Необходимо создать (не программно) текстовый файл, 
    где каждая строка описывает учебный предмет и наличие лекционных, 
    практических и лабораторных занятий по этому предмету и их количество. 
    Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
    Сформировать словарь, 
    содержащий название предмета и общее количество занятий по нему. 
    Вывести словарь на экран.
    Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —


    Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

result = {}
with open(f'text_6.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace('-', ' ').replace('(', ' ').split()
        result[line[0]] = sum(int(i) for i in line if i.isdigit())

print(result)

print('----------- Вариант ----------')


dic = {}
file = open("text_6.txt", encoding='utf-8')
lines = file.readlines()
for line in lines:
    data = line.replace('(', ' ').split()
    s = []
    for i in data:
        if i.isdigit() == True:
            s.append(int(i))
    dic[data[0]] = sum(s)
for i in dic:
    print(i, dic[i], 'lessons')
print(dic)
file.close()

print('----------- Вариант ----------')

mydict = {}
with open(f'text_6.txt', encoding='utf-8') as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        # '9' >= i >= '0' Выбрать "(число)"
        mydict[name] = name_sum

print(f"{mydict}")

print('----------- Вариант ----------')

with open(f'text_6.txt', 'r', encoding='utf-8') as file:
    a = file.readlines()
    for s in a:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in s)
        new_2 = [int(i) for i in new_str.split()]
        print(f'{s.split()[0]} {sum(new_2)}')

print('----------- Вариант ----------')

dic = {}
numbers = "123456789 0" # 0-9 с пробелом

with open(f'text_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        head, hours = line.split(':')
        dic[head] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(dic)

print('----------- Вариант ----------')

result = {}

with open(f'text_6.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        lesson_timing = []
        lesson = ([el for el in line.split(" ")])
        for el in  lesson:
            lesson_timing.append(''.join(i for i in list(el) if i.isdigit()))
        result[line.split(':')[0]] = sum([int(i) for i in lesson_timing if i.isdigit()])

print(result)
            
print('----------- Вариант re Модуль----------')

import re

subs_total_hours = {}
with open(f'text_6.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        subs_total_hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line))) 
    

print(subs_total_hours)




    
    
