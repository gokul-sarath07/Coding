# Minimum Height Binary Search Tree
# Example:
# Array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Tree:
#                5
#           2         8
#         1  3      6   9
#             4      7   10
#
# In-Order-Traversal: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ==============================================================

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

    def insertRecursion(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insertRecursion(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insertRecursion(value)

    def inOrder(self, node, values = []):
        if node:
            self.inOrder(node.left, values)
            values.append(node.value)
            self.inOrder(node.right, values)
        return values

# ==============================================================

# O(Nlog(N)) Time | O(N) Space

def minHeightBST(array):
    return minHeightBSTHelper(array, None, 0, len(array) - 1)

def minHeightBSTHelper(array, bst, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return
    midIdx = (leftIdx + rightIdx) // 2
    midValue = array[midIdx]
    if bst is None:
        bst = BST(midValue)
    else:
        bst.insert(midValue)
    minHeightBSTHelper(array, bst, leftIdx, midIdx - 1)
    minHeightBSTHelper(array, bst, midIdx + 1, rightIdx)
    return bst

# ==============================================================

# O(N) Time | O(N) Space

def minHeightBST_2(array):
    return minHeightBSTHelper_2(array, None, 0, len(array) - 1)

def minHeightBSTHelper_2(array, bst, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return
    midIdx = (leftIdx + rightIdx) // 2
    midValue = BST(array[midIdx])
    if bst is None:
        bst = midValue
    else:
        if midValue < bst.value:
            bst.left = midValue
            bst = bst.left
        else:
            bst.right = midValue
            bst = bst.right
    minHeightBSTHelper_2(array, bst, leftIdx, midIdx - 1)
    minHeightBSTHelper_2(array, bst, midIdx + 1, rightIdx)
    return bst

# ==============================================================

# O(N) Time | O(N) Space

def minHeightBST_3(array):
    return minHeightBSTHelper_3(array, 0, len(array) - 1)

def minHeightBSTHelper_3(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return
    midIdx = (leftIdx + rightIdx) // 2
    bst = BST(array[midIdx])
    bst.left = minHeightBSTHelper_3(array, leftIdx, midIdx - 1)
    bst.right = minHeightBSTHelper_3(array, midIdx + 1, rightIdx)
    return bst

height = minHeightBST_3([1,2,3,4,5,6,7,8,9,10])
print(height.inOrder(height))
