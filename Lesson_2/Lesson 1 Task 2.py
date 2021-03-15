"""
     Для списка реализовать обмен значений соседних элементов, т.е. 
     Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
     При нечетном количестве элементов последний сохранить на своем месте. 
     Для заполнения списка элементов необходимо использовать функцию input().
"""

a = input('ввести цифры через пробел ')
a = a.split()
i = 0
for x in range(len(a) // 2):
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 2
print(a)

a = list(input('Enter number without space (без пробела) - '))
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(a)

a = input('ввести цифры через пробел ').split()

if len(a) % 2 == 0:
    len_a = len(a)
else:
    len_a = len(a) - 1
"""
     Тоже самое в кратком
     len_a = len(a) if len(a) % 2 == 0 else len(a) -1
"""


a[:len_a:2], a[1:len_a:2] = a[1:len_a:2], a[:len_a:2]
print(f"Изменённый список: {a}")

a = input('ввести цифры через пробел (pop) ').split()
for i in range(1, len(a), 2):
     a.insert(i - 1, a.pop(i))
print(a)
