import logging


def transpose_matrix(matrix):
    if not matrix:
        logging.error("Матрица пустая.")
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Запуск программы для транспонирования матрицы."
    )
    parser.add_argument(
        "--matrix", type=str, help="Матрица в виде строки, разделенная запятыми"
    )
    args = parser.parse_args()

    matrix_str = args.matrix or "1,2,3;4,5,6"
    # по умолчанию используем матрицу [[1, 2, 3], [4, 5, 6]]

    matrix = [[int(num) for num in row.split(",")] for row in matrix_str.split(";")]
    logging.basicConfig(level=logging.INFO)

    result = transpose_matrix(matrix)
    logging.info(f"Транспонированная матрица: {result}")
