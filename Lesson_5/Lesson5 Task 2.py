"""
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
    выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open (f"ozon.txt", "r", encoding='utf-8') as fl:
    useful = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов'
              for line, count in enumerate(fl, 1)]
    print(*useful, f'Всего строк - {len(useful)}.', sep='\n')
    
#------------
file = open(f"ozon.txt", "r", encoding='utf-8')
data = file.readlines()
print("В файле ", len(data), "строк.")
x = 0
for i in data:
    x += 1
    #print('В', x, 'строке', len(i), 'Букв.')
file.close()
file = open(f"ozon.txt", "r", encoding='utf-8')
n = 0
while x > 0:
    x -= 1
    n += 1
    data = file.readline()
    data = data.split()
    print('В', n, 'строке', len(data), 'слов.')
file.close()

#--------------

with open (f"ozon.txt", "r", encoding='utf-8') as file:
    my_line = file.readlines()
    for index, value in enumerate(my_line, 1):
        number_of_words = len(value.split())
        print(f"Строка {index} содержит {number_of_words} слов")

