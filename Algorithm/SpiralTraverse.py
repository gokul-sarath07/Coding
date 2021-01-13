# Spiral Traverse
# Example:
# Matrix: [[1,2,3],[4,5,6],[7,8,9]]
# Answer: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# ==============================================================

# O(N) Time | O(N) Space

def spiralTraverse(matrix):
    flatten = []
    startRow, endRow = 0, len(matrix) - 1
    startCol, endCol = 0, len(matrix[0]) - 1
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            flatten.append(matrix[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            flatten.append(matrix[row][endCol])

        for col in reversed(range(startCol, endCol)):
            flatten.append(matrix[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            flatten.append(matrix[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
    return flatten

# ==============================================================

# O(N) Time | O(N) Space

def spiralTraverseRecursive(matrix):
    flatten = []
    spiralTraverseRecursiveHelper(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, flatten)
    return flatten

def spiralTraverseRecursiveHelper(matrix, startRow, endRow, startCol, endCol, flatten):
    if startRow > endRow or startCol > endCol:
        return

    for col in range(startCol, endCol + 1):
        flatten.append(matrix[startRow][col])

    for row in range(startRow + 1, endRow + 1):
        flatten.append(matrix[row][endCol])

    for col in reversed(range(startCol, endCol)):
        flatten.append(matrix[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
        flatten.append(matrix[row][startCol])

    spiralTraverseRecursiveHelper(matrix, startRow + 1, endRow - 1, startCol + 1, endCol - 1, flatten)

print(spiralTraverseRecursive([[1,2,3],[4,5,6],[7,8,9]]))
