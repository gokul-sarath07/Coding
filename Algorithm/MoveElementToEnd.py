# Move Element To Last
# Example:
# Array: [2, 1, 2, 2, 2, 3, 4, 2], Target: 2
# Answer: [1, 3, 4, 2, 2, 2, 2, 2]

# ==============================================================

# O(N) Time | O(1) Space

def moveElementToEnd(array, target):
    left = 0
    right = len(array) - 1
    while left < right:
        while left < right and array[right] == target:
            right -= 1
        if array[left] == target:
            swap(left, right, array)
        left += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
