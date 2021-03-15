"""
    6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и 
    возвращающую его же, но с прописной первой буквой. Например, print(int_func('text')) -> Text.
    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
    Каждое слово состоит из латинских букв в нижнем регистре. 
    Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
    Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(word):
    latin_char = 'qwertyuioplkjhgfdsazxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Enter words with a spaces(lower latin script): ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')

#------------------

def int_func(tx):
    return tx.capitalize()

a = input('hello world: ')
a = a.split()

for i in a:
    print(int_func(i))

#----------------

def int_func():
    for word in input('Enter words with a spaces(lower latin script):\n').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - only small English letters")
    
int_func()    
    
#---------------
def int_func():
    a = input().title().split()
    x = len(a)
    y = []
    while x > 0:
        x -= 1
        for i_2 in a[x - 1]:

            if ord(i_2) > 122:
                y.append(x - 1)
    y = set(y)
    b = []
    for x in y:
        b.append(a[x])
    a = set(a)
    b = set(b)
    a.difference_update(b)
    a = list(a)
    a = ' '.join(a)
    return a

print(int_func())

#--------------






