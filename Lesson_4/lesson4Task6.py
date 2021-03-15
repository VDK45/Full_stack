"""
    6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools. 
    Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
    Необходимо предусмотреть условие его завершения.
    Например, в первом задании выводим целые числа, 
    начиная с 3, а при достижении числа 10 завершаем цикл. 
    Во втором также необходимо предусмотреть условие, 
    при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle, islice

print('Первые 10 чисел начиная с вводимого')
iterator = count(int(input('Введите число')))

for i in range(10):
    print(next(iterator))

lst = ['string', 45, 36.6, 100]
iterator = cycle(lst)
print('Перебираем список 2 раза')
for i in range(len(lst)*2):
    print(next(iterator), end='')

#----------------------------

for i in count(int(input('\nСтартовое число: '))):
    print(i, end='')
    quit = input(' q выход: ')
    if quit == "q":
        break

my_count = count(7) # Начинает с 7
my_cycle = cycle('ABC') # элементы списка

for _ in range(3): # 3 элемента
    print(f"(my_count, my_cycle) = ({next(my_count)}, {next(my_cycle)})")
#---------------------------------

def unexpected(start, stop, num):
    try:
        start, stop, num = int(start), int(stop), int(num)
        my_list = [el for el in islice(count(), start, stop + 1)]
        r_list = iter(el for el in cycle(my_list))
        repeat_list = [next(r_list) for _ in range(num)]
        print(my_list)
        return repeat_list
    except ValueError:
        return 'Value Error'
    
print(unexpected(input('Start: '), input('Stop: '), input('Number of repetition: ') ) )


#--------------------------------

a = input('Введите 2 цифры через пробел: ').split()
lst = []
def count_func(start, stop):
    for el in count(start):
        if el > stop:
            break
        else:
            print(el)
            lst.append(el)
    return lst


def cycle_func(lst, iteration):
    i=0
    iter = cycle(lst)
    while i < iteration:
        print(next(iter))
        i += 1

count_func(int(a[0]), int(a[-1]))
cycle_func(lst, iteration = int(input('Показать сколько элементов: ')) )

#----------------------Допольнительные материалы--------


d = (el for el in count(int(a[0])) if el < int(a[-1])+1)
print(d)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
a = input('После 6 next')
