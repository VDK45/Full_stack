"""
    2. Реализовать функцию, принимающую несколько параметров,
    описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
"""

def person(name, first_name, email, tel, year, city):
    print_pers = 'ФИО. {} {} Родились в {} года. Проживаете в городе {}. Ваша почта. {}, тел. {} '.format(name,
                                                                                                          first_name,
                                                                                                          year, city,
                                                                                                          email, tel)
    return print_pers


try:
    print(person(name=input('Имя: ').lower().title(), first_name=input('Фамиля: ').lower().title(),
                 year=int(input("Год рождения: ")),
                 city=input('Город проживания: ').lower().title(),
                 email=input('Ваш email: ').lower(), tel=int(input('Тел: '))))
except ValueError:
    print('Вы ввели не число')




def personal_info(**kwargs):
    return '  '.join(kwargs.values())

print(personal_info(name=input('Name '), surname=input('Surname '),
      birtday=input('Birtday '), city=input('City '), email=input('Email: '),
      phone=input('Phone number: ')))
    



