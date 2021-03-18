"""
    7. Создать (не программно) текстовый файл, 
    в котором каждая строка должна содержать данные о фирме: 
    название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
    а также среднюю прибыль. Если фирма получила убытки, 
    в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь 
    с фирмами и их прибылями, а также словарь со средней прибылью. 
    Если фирма получила убытки, также добавить ее 
    в словарь (со значением убытков).
    Пример списка: 
    [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:

    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

    Подсказка: использовать менеджеры контекста.
"""

import json
with open(f'text_7.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    new = {}
    new_2 ={}
    profit = []
    for line in lines:
        line = line.split()
        new[line[0]] = int(line[-2]) - int(line[-1])
        if int(line[-2]) - int(line[-1]) > 0:
            profit.append(int(line[-2]) - int(line[-1]))

profit = sum(profit) / len(profit)
new_2[('Avegare profit')] = profit
lst = [new, new_2]
# запись в файл  json
with open(f'text_7_json.json', 'w', encoding='utf-8') as json_file:
    json.dump(lst,json_file, ensure_ascii=False, indent=4)
# ensure_asc = Falsei русские буквы
# indent=4 (4) отступы {}

# читать с файла text_7_json.json
with open(f'text_7_json.json', 'r', encoding='utf-8') as json_fl:
    print(json_fl.read())

print('---------------- Вариан ------------------')

with open(f'my_json_7.json', 'w', encoding='utf-8') as write_f:
    with open(f'text_7.txt', 'r', encoding='utf-8') as f_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        result = [profit, {"avegare_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, write_f, ensure_ascii=False, indent=4)
                           
# читать с файла my_json_7.json
with open(f'my_json_7.json', 'r', encoding='utf-8') as json_fl:
    print(json_fl.read())                                   
                                       






