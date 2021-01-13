# Binary Search Tree Traversal Algorithms
# Example:          Answer:
#        10          Pre-Order: [10, 5, 2, 1, 5, 15, 22]
#     5     15        In-Order: [1, 2, 5, 5, 10, 15, 22]
#   2   5     22    Post-Order: [1, 2, 5, 5, 22, 15, 10]
# 1

# ==============================================================

# O(N) Time | O(D) Space

def preOrderTraversal(tree, array = []):
    if tree is not None:
        array.append(tree.value)
        preOrderTraversal(tree.left, array)
        preOrderTraversal(tree.right, array)
    return array

# O(N) Time | O(D) Space

def inOrderTraversal(tree, array = []):
    if tree is not None:
        inOrderTraversal(array.left, array)
        array.append(tree.value)
        inOrderTraversal(array.right, array)
    return array

# O(N) Time | O(D) Space

def postOrderTraversal(tree, array = []):
    if tree is not None:
        postOrderTraversal(tree.left, array)
        postOrderTraversal(tree.right, array)
        array.append(tree.value)
    return array
