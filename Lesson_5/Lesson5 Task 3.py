"""
    3. Создать текстовый файл (не программно), 
    построчно записать фамилии сотрудников и величину их окладов. 
    Определить, кто из сотрудников имеет оклад менее 20 тыс., 
    вывести фамилии этих сотрудников. 

    Выполнить подсчет средней величины дохода сотрудников.
"""

with open(f"text_3.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    salary_all = []
    for i in lines:
        i = i.split()
        salary_all.append(float(i[1]))
        if float(i[-1]) < 20000:
            print(f"{i[0]} получает {i[-1]} руб")

print(f'Средняя зарплата: {sum(salary_all) / len(salary_all)}')
    
print('------------- Вариант -------------')

with open(f"text_3.txt", "r", encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Average with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

print('------------- Вариант -------------')

def task_3():
    wages = {} # Словар (dict)
    try:
        with open(f"text_3.txt", "r", encoding='utf-8') as file:
            for line in file:
                wages[line.split()[0]] = float(line.split()[1]) # Добавление в слоаврь (dict)
        print(f'Меньше 20000 получают: ')
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата: {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Ошибка с чтением файла!')
    except:
        print('Ошибка')

task_3()

        



