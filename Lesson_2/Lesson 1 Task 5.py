"""
    Реализовать структуру «Рейтинг»,
    представляющую собой не возрастающий набор натуральных чисел.
    У пользователя необходимо запрашивать новый элемент рейтинга.
    Если в рейтинге существуют элементы с одинаковыми значениями,
    то новый элемент с тем же значением должен разместиться после них.
    Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
    Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
    Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
    Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
    Набор натуральных чисел можно задать непосредственно в коде, например,
    my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 7, 7, 5, 3, 3, 2]
new_number = float(input('Введиде номер '))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)

'''
    мой не правильный способ
'''

lst = [7, 7, 5, 3, 3, 2]
a = float(input('Enter number: '))
for d, i in enumerate(lst, 0):
    if a > lst[d]:
        lst.insert(d, a)
        break
    elif a < lst[d] and a > lst[d+1]:
        lst.insert(d+1, a)
        break
    elif a == lst[d] and a == lst[d+1]:
        lst.insert(d+2, a)
        break
    elif a <= lst[-1]:
        lst.append(a)
        break
    elif a == lst[d]:
        lst.insert(d+1, a)
        break
    
print(lst)




