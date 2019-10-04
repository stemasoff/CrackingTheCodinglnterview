'''
Реализуйте алгоритм, определяющий, все л и символы в строке встречаются
только один раз. А если при этом запрещено использование дополнительных
структур данных?
'''
string = 'abcjdjs'
for i in range(len(string)):
    if string.count(string[i]) > 1 and string.index(string[i]) == i:
        print('{} встречается больше одного раза'.format(string[i]))
