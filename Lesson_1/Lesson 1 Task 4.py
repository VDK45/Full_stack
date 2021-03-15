"""
    4. Пользователь вводит целое положительное число. 
    Найдите самую большую цифру в числе. 
    Для решения используйте цикл while и арифметические операции.
"""

num_init = int(input('Enter number: '))
greates = 0
num = num_init

while num > 0:
    digit = num % 10  # Определяем последнюю цифру
    if digit > greates:
        greates = digit
    num = num // 10  # отсекаем от числа последнюю цифру
print(f'Greates number {greates} in {num_init}')

#------------- Ещё не дошли до функции с рекурсией -----------

def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > num % 10 else num % 10

number = int(input('Enter the number: '))
print(f'The largest number is: {num_max(number)}')


