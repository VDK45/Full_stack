"""
    Создать список и заполнить его элементами различных типов данных. 
    Реализовать скрипт проверки типа данных каждого элемента. 
    Использовать функцию type() для проверки типа. 
    Элементы списка можно не запрашивать у пользователя, а указать явно, 
    в программе.
"""


lst = [(-1 + 0j), 1, 4.5, True, None, 'string', [2, 6], (6, 7, 8),
       {1: 'a', 2: 'b'}, {9, 10}, frozenset(), range(11), b'twelve',
       bytearray(b'thirteen'), zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]
for i, item in enumerate(lst, 1):
    print(f"{i}...{item} - {type(item)}")
    
    
'''
    Пример с enumerate
'''
list1 = ['str1', 'str2', 'str3']

for position, string in enumerate(list1, 100): # position начинает с 100
     print(position, string)
     