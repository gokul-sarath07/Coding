# Binary Search Tree Construction
# Methods Included: Insertion, Searching, Remove, In-Order Traversal,
#                   Validate BST

# ==============================================================

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#   Average: O(log(N)) Time | O(1) Space
#   Worst:   O(N) Time | O(1) Space

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

#   Average: O(log(N)) Time | O(1) Space
#   Worst:   O(N) Time | O(1) Space

    def contains(self, value):
        currentNode = self
        while currentNode:
            if value == currentNode.value:
                return True
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False

#   Average: O(log(N)) Time | O(1) Space
#   Worst:   O(N) Time | O(1) Space

    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getSmallestValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is None else currentNode.right
                break
        return self


    def getSmallestValue(self):
        currentNode = self
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode.value

#   O(N) Time | O(H) Space

    def inOrderTraversal(self, root, values = []):
        if root:
            self.inOrderTraversal(root.left, values)
            values.append(root.value)
            self.inOrderTraversal(root.right, values)
        return values

    def validateBST(self, tree):
        if tree:
            if tree.left is None or tree.right is None:
                return True
            if tree.left.value > tree.value or tree.value > tree.right.value:
                return False
            else:
                self.validateBST(tree.left)
                self.validateBST(tree.right)
        return True

root = BST(6)
root.insert(3).insert(2).insert(4).insert(5).insert(9).insert(7).insert(8).insert(10).insert(1)
print(root.inOrderTraversal(root))
# root.remove(2).remove(4)
# print(root.contains(3))
print(root.validateBST(root))
