"""
    6. Спортсмен занимается ежедневными пробежками. 
    В первый день его результат составил a километров. 
    Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
    Требуется определить номер дня, 
    на который общий результат спортсмена составить не менее b километров. 
    Программа должна принимать значения параметров a и b и выводить 
    одно натуральное число — номер дня.
    Например: a = 2, b = 3.
    Результат:
    1-й день: 2
    2-й день: 2,2
    3-й день: 2,42
    4-й день: 2,66
    5-й день: 2,93
    6-й день: 3,22
"""

while True:
    days = 1
    start = float(input("Стартовый результат: "))
    last = float(input("Финальный результат: "))
    if start <= 0 or last < 0:
        print("Вы ввели меньше нуля!")
    else:
        while start < last:
            start += start * 0.1
            days += 1
        print(f'Результат достигнет  за {days} дней')
        break
