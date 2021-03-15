
"""
    1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def dev(x, y):
    try:
        c = x / y
    except ZeroDivisionError:
        print('Error')
        c = 0
    try:
        d = y / x
    except ZeroDivisionError:
        print('Error')
        d = 0
    return print(f"резултат x/y = {round(c, 4)} и y/x = {round(d, 4)}")
class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt
    
a = input("x, y: ").split()
try:
    a = a
    if len(a) > 2:
        raise MyError('Введите только 2 числа')
except (ValueError, MyError) as err:
    print(err)
    
try:
    dev(int(a[0]), int(a[1]))
except ValueError:
    dev(0, 0)
    print("Вы ввели не цифры ")
