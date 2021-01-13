# Rives Sizes
# Example:
# Matrix: [[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]]
#
#   1 0 0 1 0   Rivers: 1   1   1       1   1
#   1 0 1 0 0           1       1       1   1
#   0 0 1 0 1                   1
#   1 0 1 0 1                   1 1
#   1 0 1 1 0
#                      [2,  1,  5,      2,  2]
#
# Answer: [2, 1, 5, 2, 2]

# ==============================================================

# O(WH) Time | O(WH) Space || WH being Width*Height of Matrix

def riverSize(matrix):
    sizes = []
    visited = [[False for values in rows] for rows in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if visited[row][col]:
                continue
            traverseNode(row, col, matrix, visited, sizes)
    return sizes

def traverseNode(row, col, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[row, col]]
    while len(nodesToExplore):
        nodeInfo = nodesToExplore.pop()
        row, col = nodeInfo[0], nodeInfo[1]
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(row, col, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbors(row, col, matrix, visited):
    unvisitedNeighbors = []
    if row > 0 and not visited[row - 1][col]:
        unvisitedNeighbors.append([row - 1, col])
    if row < len(matrix) - 1 and not visited[row + 1][col]:
        unvisitedNeighbors.append([row + 1, col])
    if col > 0 and not visited[row][col - 1]:
        unvisitedNeighbors.append([row, col - 1])
    if col < len(matrix[row]) - 1 and not visited[row][col + 1]:
        unvisitedNeighbors.append([row, col + 1])
    return unvisitedNeighbors

matrix = [[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]]
print(riverSize(matrix))
