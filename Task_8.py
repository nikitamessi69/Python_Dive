# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transpose_matrix(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

matrix = [[1, 2, 3], [4, 5, 6]]
result = transpose_matrix(matrix)
print(result)