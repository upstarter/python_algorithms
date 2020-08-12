# first two examples run in O(n^2) time, last is O(m * n)
def matrix_in_spiral_order(square_matrix: [[int]]) -> [int]:
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the matrix
            spiral_ordering.append(square_matrix[offset][offset])
            return

        # add first three elements of the first row (1,2,3)
        spiral_ordering.extend(square_matrix[offset][offset : -1 - offset])

        # add first three elements of the last column (4,8,12), zip transposes matrix
        # so last col is first row
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset : -1 - offset]
        )

        # last three elements of the last row (16,15,14)
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset : offset : -1])

        # last three elements of the first column (13, 9, 5)
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset : offset : -1]
        )

    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering


square_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix_in_spiral_order(square_matrix))


# The above works in four almost identical iterations, Now a solution with a single iteration:

def matrix_in_spiral_order_single_iter(square_matrix: [[int]]) -> [int]:
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]

        if (
            next_x not in range(len(square_matrix))
            or next_y not in range(len(square_matrix))
            or square_matrix[next_x][next_y] == 0
        ):
            direction = (direction + 1) & 3
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


square_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix_in_spiral_order_single_iter(square_matrix))

# O(m * n) time, O(1) space
def spiralCopy(inputMatrix):
    n = len(inputMatrix)
    m = len(inputMatrix[0])

    topRow = 0
    btmRow = n - 1
    leftCol = 0
    rightCol = m - 1
    result = []

    while (topRow <= btmRow) and (leftCol <= rightCol):
        # copy the next top row
        for i in range(leftCol, rightCol + 1):
            result.append(inputMatrix[topRow][i])
        topRow += 1

        # copy the next right hand side column
        for i in range(topRow, btmRow + 1):
            result.append(inputMatrix[i][rightCol])
        rightCol -= 1

        # copy the next bottom row
        if topRow <= btmRow:
            for i in range(rightCol, leftCol - 1, -1):
                result.append(inputMatrix[btmRow][i])
            btmRow -= 1

        # copy the next left hand side column
        if leftCol <= rightCol:
            for i in range(btmRow, topRow - 1, -1):
                result.append(inputMatrix[i][leftCol])
            leftCol += 1

    return result


square_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(spiralCopy(square_matrix))
