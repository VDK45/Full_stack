"""
    4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, 
    открывающую файл на чтение и считывающую построчно данные. 
    При этом английские числительные должны заменяться на русские. 
    Новый блок строк должен записываться в новый текстовый файл.
"""

a = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open(f"text_4.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    for i in lines:
        i = i.split()
        for j in a.keys():
            if j == i[0]:
                print(f'{a.get(j)} - {i[-1]}')


print('------------- Вариант рабочий? ------------')
rus_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open(f"text_4_new.txt", "w", encoding='utf-8') as new_file:
    with open(f"text_4.txt", encoding='utf-8') as my_file:
        new_file.writelines([line.repleace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])

print('------------- Вариант рабочий? ------------')

# pip install googletrans
from googletrans import Translator

with open(f"text_4_translator.txt", "w", encoding='utf-8') as f:
    with open(f"text_4.txt", "r", encoding='utf-8') as f1:
        text = f1.read()
    try:
        f.write(Translator().translate(text, dest='ru').text)
    except ArtributeError:
        print("Нет связи с Google, перевод не доступен")
    
