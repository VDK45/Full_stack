"""
    4. Программа принимает действительное положительное число x и целое отрицательное число y. 
    Необходимо выполнить возведение числа x в степень y. 
    Задание необходимо реализовать в виде функции my_func(x, y). 
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


x = lambda x, y: x**y
print(x(2.5,-4))

#-------------
def my(x, y):
    return print(x**y)
my(2.5, -4)

#----------------
def my_func(x, y):
    try:
        x = float(input('Number X > 0: '))
        y = int(input('Number y < 0: '))
    except ValueError:
        print('Wrong number!')
    if x > 0 and y < 0:
        y = abs(y)
        a = x
        for i in range(y - 1):
            a *= x
        # result = 1 / (x ** abs(y))
        return print('{} степенью -{} будет  {}'.format(x, y, 1 / a))
    else:
        print('Need x > 0 and y < 0')


my_func(2.5, -4)

#------------- Рекурсия и тернарная операция-----
def my_func(x, y):
    return 1 if y == 0 else my_func(x, y + 1) * 1 / x

a = 2.5
b = -4
print(f'{a} в степени {b} = {my_func(a, b)}')

#-------------
def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'x небольше нуля\ny не меньше нуля'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат: {result}'
    except ValueError:
        return 'Numers only'
n_1 = input('Действительное положительное число: ')    
n_2 = input('Целое отрицательное число: ')
print(my_func2(n_1, n_2))


