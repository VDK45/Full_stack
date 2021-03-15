"""
    3. Реализовать функцию my_func(), которая принимает 
    три позиционных аргумента, 
    и возвращает сумму наибольших двух аргументов.
"""

def my_func(n_1, n_2, n_3):
    my_list = [n_1, n_2, n_3]
    try:
        my_list.remove(min(my_list)) # удалит минимальную
        return sum(my_list)
    except TypeError:
        return "Only a number!"
print(my_func(4, 5, -45))

def my_func(num_1, num_2, num_3):
    return sum(sorted([num_1, num_2, num_3])[1:]) # sorted 1ый < 2ой < 3ий
print(my_func(4, 5, -45))

my_func = lambda arg_1, arg_2, arg_3: (arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)
print(my_func(4, 5, -45))


def my_func(x, y, z):
    if x > y and z > y:
        return print(x + z)
    elif x > z and y > z:
        return print(x + y)
    elif y > x and z > x:
        return print(y + z)
while 1:
    a = input('X Y Z: ').split()
    if a[0] == 'q':
        break
    my_func(int(a[0]), int(a[1]), int(a[2]))

