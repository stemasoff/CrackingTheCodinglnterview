'''
Напишите функцию, которая проверяет, является ли заданная строка переста­
новкой палиндрома. (Палиндром - слово или фраза, одинаково читающиеся
в прямом и обратном направлении; перестановка - строка, содержащая те
же символы в другом порядке.) Палиндром не ограничивается словами из
словаря.
'''
string = '1 101 11'
def palindrome_check(x):
    x = x.replace(' ', '')
    cnt = 0
    for i in x:
        if x.count(i) % 2 != 0 and cnt == 1:
            return 'Строка не является перестановкой палиндрома'
        elif x.count(i) % 2 != 0:
            cnt = 1

    return 'Строка является перестановкой палиндрома'
print(palindrome_check(string))