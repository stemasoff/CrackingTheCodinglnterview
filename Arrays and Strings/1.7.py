from copy import copy
'''
Имеется изображение, представленное матрицей NxN; каждый пиксел пред­
ставлен 4 байтами. Напишите метод для поворота изображения на 90 градусов.
У дастся ли вам выполнить эту операцию «на месте»?
'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_matrix = copy(matrix)
for i in matrix:
    print(*i)

for i in range(len(matrix)):
    for j in range(len(matrix)-1, -1, -1):
        new_matrix[i][j] = matrix[j][i]
        print(j, i)



for i in new_matrix:
    print(*i)