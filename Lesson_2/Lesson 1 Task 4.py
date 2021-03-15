"""
     Пользователь вводит строку из нескольких слов, разделённых пробелами.
     Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
     Если в слово длинное, выводить только первые 10 букв в слове.
"""

l = input('Hi: ').split()
for d, i in enumerate(l, 1):
    if len(i) > 5:
        print(d, i[:5])
    else:
        print(d, i)

l2 = input('Hi: ').split()
for d, i in enumerate(l2, 1):
    print(d, i[:5]) if len(i) > 5 else print(d, i)

l3 = input('Hi: ').split()
for d, i in enumerate(l3, 1):
    print(f"{d}. . .{i[:5]}")


