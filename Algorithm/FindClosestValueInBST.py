# Find Closest Value In Binary Search Tree
# Example:
# Tree:
#         10
#      4     15
#    2  3   13  22
#
# Target: 12
# Closest: 13

# ==============================================================

# O(log(N)) Time | O(log(N)) Space

def findClosestValueInBST(tree, target):
    return calculateClosestValueInBST(tree, target, float("inf"))

def calculateClosestValueInBST(node, target, closestValue):
    if node is None:
        return closestValue
    if abs(closestValue-target) > abs(node.value-target):
        closestValue = node.value
    if node.value > target:
        return calculateClosestValueInBST(node.left, target, closestValue)
    elif node.value < target:
        return calculateClosestValueInBST(node.right, target, closestValue)
    else:
        return closestValue
