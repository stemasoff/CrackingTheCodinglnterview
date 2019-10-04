'''
Для двух строк напишите метод, определяющий, явля�тся ли одна строка
перестановкой другой.
'''
string1 = '123'
string2 = '123'

def check(x, y):
    for i in x:
        if i not in y or len(x) != len(y):
            return 'Строка 2 не является перестановкой строки 1'
        elif x == y:
            return 'Строка 2 = строке 1'
    return 'Строка 2 является перестановкой строки 1'

print(check(string1, string2))