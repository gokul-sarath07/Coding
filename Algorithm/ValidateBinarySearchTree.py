# Validate Binary Search Tree
# Example:
# Tree:
#         10
#      4     15
#    2  3  13  22
#
# Answer: False

# ==============================================================

# O(N) Time | O(D) Space

def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))

def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    isLeftValid = validateBSTHelper(tree.left, minValue, tree.value)
    return isLeftValid and validateBSTHelper(tree.right, tree.value, maxValue)
