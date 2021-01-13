# Depth First Search
# Example:
# Tree:
#         10
#      4     15
#    2  3  13  22
#
# DFS: [10, 4, 2, 3, 15, 13, 22]

# ==============================================================

# O(V+E) Time | O(V) Space

def depthFirstSearch(node, valList=[]):
    if node:
        valList.append(node.value)
        depthFirstSearch(node.left, valList)
        depthFirstSearch(node.right, valList)
    return valList
