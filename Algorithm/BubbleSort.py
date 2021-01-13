# Bubble Sort Algorithm
# Example:
# Array: [141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]
# Answer: [-27, -17, -7, 1, 7, 7, 8, 17, 18, 141, 541]

# ==============================================================

# O(N^2) Time | O(1) Space

def bubbleSort(array):
    isSorted = False
    ignoredValues = 1
    while not isSorted:
        isSorted = True
        for idx in range(len(array) - ignoredValues):
            if array[idx] > array[idx + 1]:
                swapValues(array, idx, idx + 1)
                isSorted = False
        ignoredValues += 1
    return array

def swapValues(array, x, y):
    array[x], array[y] = array[y], array[x]

print(bubbleSort([141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]))
