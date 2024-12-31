# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/5454803700023296


def rotate_image(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix


if __name__ == "__main__":
    for matrix in [
        [
            [3],
        ],
        [
            [2, 6],
            [3, 4],
        ],
        [
            [2, 6, 8],
            [3, 4, 8],
            [9, 8, 8],
        ],
        [
            [2, 6, 8, 3],
            [3, 4, 8, 1],
            [9, 8, 8, 2],
            [7, 3, 5, 4],
        ],
        [
            [3, 6, 7, 2, 4],
            [3, 3, 7, 5, 2],
            [4, 7, 9, 3, 3],
            [9, 10, 5, 7, 3],
            [9, 9, 7, 7, 4],
        ],
    ]:
        print(f"{matrix} --> {rotate_image(matrix)}")
