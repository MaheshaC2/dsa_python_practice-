# Problem: Rotate Matrix by 90 Degrees
# Category: Matrix
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix
