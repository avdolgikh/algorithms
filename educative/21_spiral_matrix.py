# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/6183529995829248


# def spiral_order(matrix):
#     result = []
#     top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

#     while top <= bottom and left <= right:
#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1
#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1
#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[bottom][i])
#             bottom -= 1
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1

#     return result


def spiral_order(matrix):
    result = []
    while matrix:
        # Add the first row
        result += matrix.pop(0)
        # Add the last column
        if matrix and matrix[0]:
            result += [row.pop() for row in matrix]
        # Add the last row in reverse
        if matrix:
            result += matrix.pop()[::-1]
        # Add the first column in reverse
        if matrix and matrix[0]:
            result += [row.pop(0) for row in matrix[::-1]]
    return result


if __name__ == "__main__":
    for matrix in [
        [
            [3],
        ],
        [
            [2, 6],
        ],
        [
            [2],
            [6],
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
            [2, 6],
            [3, 4],
            [9, 8],
        ],
        [
            [2, 6, 8],
            [3, 4, 8],
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
        [
            [3, 6, 7, 2, 4],
            [3, 3, 7, 5, 2],
            [4, 7, 9, 3, 3],
        ],
        [
            [3, 6, 7],
            [3, 3, 7],
            [4, 7, 9],
            [9, 10, 5],
            [9, 9, 7],
        ],
        [[-94,75],[58,-95],[15,-91],[-100,58],[83,98]],
    ]:
        print(f"{matrix} --> {spiral_order(matrix)}")
