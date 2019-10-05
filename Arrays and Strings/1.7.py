'''
Имеется изображение, представленное матрицей NxN; каждый пиксел пред­
ставлен 4 байтами. Напишите метод для поворота изображения на 90 градусов.
У дастся ли вам выполнить эту операцию «на месте»?
'''
from copy import deepcopy
matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_matrix = deepcopy(matrix)
for i in matrix:
    print(*i)

for i in range(len(matrix)):
    temp_index = 0
    for j in range(len(matrix)-1, -1, -1):
        print('Мы меняем [{},{}] на [{},{}]'.format(i, temp_index, j, i))
        print('Поменяли {} на {}'.format(new_matrix[i][temp_index], matrix[j][i]))
        new_matrix[i][temp_index] = matrix[j][i]
        temp_index += 1



for i in new_matrix:
    print(*i)

