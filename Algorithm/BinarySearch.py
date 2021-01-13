# Binary Search Algorithm
# Example:
# Array: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], Target: 33
# Answer: True

# ==============================================================

# O(log(N)) Time | O(1) Space

def binarySearch(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1
    middleIdx = 0
    while leftIdx <= rightIdx:
        middleIdx = (leftIdx + rightIdx) // 2
        if array[middleIdx] == target:
            return middleIdx
        elif array[middleIdx] < target:
            leftIdx = middleIdx + 1
        elif array[middleIdx] > target:
            rightIdx = middleIdx - 1
    return None

# ==============================================================

# O(log(N)) Time | O(log(N)) Space

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1 )

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middleIdx = (left + right) // 2
    if array[middleIdx] == target:
        return middleIdx
    elif array[middleIdx] < target:
        return binarySearchHelper(array, target, middleIdx+1, right)
    elif array[middleIdx] > target:
        return binarySearchHelper(array, target, left, middleIdx-1)


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],74))
