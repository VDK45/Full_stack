"""
    2. Пользователь вводит время в секундах. 
    Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
    Используйте форматирование строк.
"""

time = int(input('Enter the time in seconds: '))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# Не более 24 часа
time2 = int(input('Enter the time in seconds: '))
hours2 = (time2 // 3600) % 24
minutes2 = (time2 % 3600) // 60
seconds2 = time % 60
print(f'{hours2:02}:{minutes2:02}:{seconds2:02}')

